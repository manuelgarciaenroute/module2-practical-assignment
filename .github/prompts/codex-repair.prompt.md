You are repairing a failing Python project in CI.

Goals:
1. Read `failing-tests.txt` to understand the test failures.
2. Diagnose the root cause.
3. Patch only application code under `scientific_calculator/` and `main.py`.
4. Do not modify tests, workflows, or documentation files.
5. Run the test suite (`python -m unittest discover -s tests -p "test_*.py"`) after changes.
6. If tests still fail, iterate until they pass or no safe fix is possible.

Output:
- Keep changes minimal and focused on the root cause.
- At the end, provide a short summary of what was fixed.

