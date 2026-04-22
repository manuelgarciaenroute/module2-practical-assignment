param(
    [int]$MaxRetries = 3
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
$PSNativeCommandUseErrorActionPreference = $false

function Resolve-PythonRunner {
    $candidates = @(
        @{Cmd = "python"; Prefix = @("python")},
        @{Cmd = "py"; Prefix = @("py", "-3")}
    )

    foreach ($candidate in $candidates) {
        try {
            & $candidate.Cmd "--version" *> $null
            if ($LASTEXITCODE -eq 0) {
                return $candidate.Prefix
            }
        }
        catch {
            continue
        }
    }

    throw "Could not find a working Python runner. Install Python and ensure 'python' or 'py -3' works."
}

function Invoke-TestSuite {
    param(
        [string[]]$PythonPrefix
    )

    $args = @()
    if ($PythonPrefix.Length -gt 1) {
        $args += $PythonPrefix[1..($PythonPrefix.Length - 1)]
    }
    $args += @("-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py")

    $previousErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = & $PythonPrefix[0] @args 2>&1 | Out-String
    }
    finally {
        $ErrorActionPreference = $previousErrorAction
    }

    return @{
        ExitCode = $LASTEXITCODE
        Output   = $output
    }
}

function Repair-FromFailure {
    param(
        [string]$FailureOutput
    )

    $operationsPath = Join-Path $PSScriptRoot "scientific_calculator\operations.py"
    if (-not (Test-Path -LiteralPath $operationsPath)) {
        throw "Cannot patch application code: $operationsPath was not found."
    }

    if ($FailureOutput -match "test_subtract") {
        Write-Host "Diagnosis: subtraction behavior is broken (test_subtract failed)."
        $content = Get-Content -LiteralPath $operationsPath -Raw
        $updated = [regex]::Replace(
            $content,
            "def subtract\(a: float, b: float\) -> float:\r?\n\s+return .+",
            "def subtract(a: float, b: float) -> float:`n    return a - b"
        )

        if ($updated -eq $content) {
            Write-Host "Repair step: no subtraction patch applied (pattern not matched)."
            return $false
        }

        Set-Content -LiteralPath $operationsPath -Value $updated -Encoding UTF8
        Write-Host "Repair step: patched scientific_calculator/operations.py (subtract)."
        return $true
    }

    Write-Host "Diagnosis: no known automatic repair rule matched current failure."
    return $false
}

try {
    $pythonPrefix = Resolve-PythonRunner
    Write-Host ("Using Python runner: " + ($pythonPrefix -join " "))
}
catch {
    Write-Error $_
    exit 1
}

for ($attempt = 1; $attempt -le $MaxRetries; $attempt++) {
    Write-Host ""
    Write-Host "Attempt $attempt/$MaxRetries - running tests..."
    $result = Invoke-TestSuite -PythonPrefix $pythonPrefix
    Write-Host $result.Output

    if ($result.ExitCode -eq 0) {
        Write-Host "Repair flow result: tests are passing."
        exit 0
    }

    Write-Host "Tests failed. Reading failures and attempting diagnosis..."
    $didPatch = Repair-FromFailure -FailureOutput $result.Output
    if (-not $didPatch) {
        Write-Host "Repair flow result: unable to auto-repair with available rules."
        exit 1
    }
}

Write-Host "Repair flow result: retry limit reached and tests are still failing."
exit 1
