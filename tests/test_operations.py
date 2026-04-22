import math
import unittest

from scientific_calculator.operations import (
    add,
    divide,
    exponential,
    logarithm,
    multiply,
    subtract,
)


class TestOperations(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(10, 4), 6)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_logarithm_default_base(self) -> None:
        self.assertTrue(math.isclose(logarithm(math.e), 1.0, rel_tol=1e-9))

    def test_logarithm_custom_base(self) -> None:
        self.assertTrue(math.isclose(logarithm(1000, 10), 3.0, rel_tol=1e-9))

    def test_logarithm_invalid_value_raises(self) -> None:
        with self.assertRaises(ValueError):
            logarithm(0)

    def test_logarithm_invalid_base_raises(self) -> None:
        with self.assertRaises(ValueError):
            logarithm(10, 1)

    def test_exponential(self) -> None:
        self.assertEqual(exponential(2, 8), 256)


if __name__ == "__main__":
    unittest.main()

