# Local Codex Repair Flow

This project includes a repeatable local repair workflow:

- Script: `codex_repair_flow.ps1`
- Goal: run tests, inspect failures, diagnose likely root cause, patch only application code, and retry.

## What The Script Does

1. Resolves a working Python runner (`python` or `py -3`).
2. Runs the test suite:
   - `python -m unittest discover -s tests -p "test_*.py"`
3. If tests fail, reads the failure output.
4. Applies a targeted repair rule for known failures (currently `test_subtract`).
5. Patches only `scientific_calculator/operations.py`.
6. Re-runs tests.
7. Stops when tests pass, no matching repair rule exists, or retry limit is reached.

## Run It

From repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\codex_repair_flow.ps1 -MaxRetries 3
```

## Expected Behavior

- If subtraction logic is intentionally broken, the script should detect `test_subtract` failure, fix `subtract`, and pass tests on a subsequent run.
- If failure output does not match a known repair rule, it exits with failure and does not modify tests.

