import io
import unittest
from unittest.mock import patch

from scientific_calculator.app import run


class TestAppFlow(unittest.TestCase):
    def test_sum_flow_prints_result(self) -> None:
        user_inputs = ["1", "2", "3", "0"]
        with patch("builtins.input", side_effect=user_inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as output:
            run()

        printed = output.getvalue()
        self.assertIn("Result: 5.0", printed)
        self.assertIn("Goodbye.", printed)

    def test_division_by_zero_displays_error(self) -> None:
        user_inputs = ["4", "10", "0", "0"]
        with patch("builtins.input", side_effect=user_inputs), patch(
            "sys.stdout", new_callable=io.StringIO
        ) as output:
            run()

        printed = output.getvalue()
        self.assertIn("Error: Division by zero is not allowed.", printed)


if __name__ == "__main__":
    unittest.main()

