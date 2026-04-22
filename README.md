# Scientific Calculator (Console)

This project is a multi-file Python console application that simulates a scientific calculator and includes local and CI repair/grading workflows.

## Prerequisites

- Python 3.13+ available as `python` (or `py -3` on Windows)
- Git
- PowerShell (for the local repair script)
- A GitHub repository with Actions enabled (for CI/auto-fix/grading workflows)

## Local Setup

1. Clone the repository and move into it.
2. (Optional) Create and activate a virtual environment.
3. Install dependencies (if a `requirements.txt` file exists).

```bash
python -m pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

Run the calculator:

```bash
python main.py
```

## How To Run Tests Locally

From the repository root:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

## How To Create A Failing Scenario

A simple failing scenario is to intentionally break an application function in `scientific_calculator/operations.py`.  
Example: change `subtract(a, b)` to return `a + b` instead of `a - b`.  
Then run tests again; `test_subtract` should fail.

## How To Run The Local Repair Workflow

The local repair workflow is implemented in:

- `codex_repair_flow.ps1`

It performs this loop:
- run tests
- read failure output
- diagnose known root cause patterns
- patch only application code
- retry until tests pass or retry limit is reached

Run it from repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\codex_repair_flow.ps1 -MaxRetries 3
```

## How To Run The GitHub Actions Auto-Fix Workflow

The auto-fix workflow is:

- `.github/workflows/codex-auto-repair.yml`

How it runs:
1. Open or update a pull request with failing code.
2. `CI` (`.github/workflows/ci.yml`) runs on the PR and fails.
3. `Codex Auto Repair` triggers via `workflow_run` after that CI failure.
4. It runs tests, invokes Codex non-interactively, applies a repair patch, commits to the same branch, and re-runs tests.

Notes:
- It is restricted to PR branches in the same repository (`head_repository.full_name == github.repository`).
- It requires repository write permission for workflow pushes.

## How The Grading Workflow Works

The grading workflow is:

- `.github/workflows/pr-grading.yml`

It runs on PR open/synchronize/reopen and comments a score out of 100 based on:
- tests pass (`+50`)
- restricted files were not modified (`+25`)
- diff is reasonably small (`<= 300` changed lines, `+25`)

Restricted paths:
- `tests/`
- `.github/workflows/`
- `.github/prompts/`
- `CodexLog.txt`

The workflow creates or updates a single PR comment with the latest score breakdown.

## Required Repository Secrets

Required for auto-fix:
- `OPENAI_API_KEY`: used by `openai/codex-action@v1` to invoke Codex.

Recommended repository settings:
- GitHub Actions workflow permissions: allow write access to repository contents (so auto-fix can commit and push).
