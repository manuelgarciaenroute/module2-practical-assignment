"""Math operations for the scientific calculator."""

from __future__ import annotations

import math


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


def logarithm(value: float, base: float = math.e) -> float:
    if value <= 0:
        raise ValueError("Logarithm input must be greater than 0.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be greater than 0 and different from 1.")
    return math.log(value, base)


def exponential(base: float, exponent: float) -> float:
    return base**exponent
