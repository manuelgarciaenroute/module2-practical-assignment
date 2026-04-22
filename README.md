# Scientific Calculator (Console)

This project is a small multi-file Python console application that simulates a scientific calculator.

## Functionality

The calculator is interactive and runs in the terminal. It asks the user to:
- choose an operation from a menu
- provide the required numeric parameters
- receive the calculated result

Supported operations:
- Sum
- Subtraction
- Multiplication
- Division
- Logarithm (natural log by default, or custom base)
- Exponential (power)

Input and validation behavior:
- numeric inputs are parsed as `float`
- invalid numeric input is re-prompted
- division by zero raises a handled error message
- invalid logarithm inputs (value <= 0, or invalid base) raise handled error messages

## Project Structure

- `main.py`: application entry point
- `scientific_calculator/app.py`: menu and interactive application flow
- `scientific_calculator/operations.py`: math operation functions
- `scientific_calculator/ui.py`: console input helper functions
- `tests/test_operations.py`: unit tests for calculator logic
- `tests/test_app_flow.py`: tests for interactive console flow using mocked input/output

## How To Run

Run the app from the project root:

```bash
python main.py
```

## Tests

The test suite uses Python's built-in `unittest` framework.

Run tests from the project root:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### What Is Tested

`tests/test_operations.py` verifies:
- correct arithmetic results for sum, subtraction, multiplication, division
- division-by-zero error handling
- logarithm correctness for natural and custom-base logs
- logarithm invalid input/base error handling
- exponential correctness

`tests/test_app_flow.py` verifies:
- the interactive sum flow prints the expected result
- division by zero in the interactive flow prints the expected error

These tests are meaningful regression checks and will fail if core calculator behavior is intentionally broken.

