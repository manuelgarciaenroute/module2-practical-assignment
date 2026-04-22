"""Main application flow for the scientific calculator."""

from __future__ import annotations

import math

from scientific_calculator.operations import (
    add,
    divide,
    exponential,
    logarithm,
    multiply,
    subtract,
)
from scientific_calculator.ui import read_float, read_text


def show_menu() -> None:
    print("\nScientific Calculator")
    print("---------------------")
    print("1) Sum")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Logarithm")
    print("6) Exponential")
    print("0) Exit")


def run() -> None:
    while True:
        show_menu()
        option = read_text("Select an option: ")

        if option == "0":
            print("Goodbye.")
            break

        try:
            if option == "1":
                a = read_float("First number: ")
                b = read_float("Second number: ")
                result = add(a, b)
            elif option == "2":
                a = read_float("First number: ")
                b = read_float("Second number: ")
                result = subtract(a, b)
            elif option == "3":
                a = read_float("First number: ")
                b = read_float("Second number: ")
                result = multiply(a, b)
            elif option == "4":
                a = read_float("Dividend: ")
                b = read_float("Divisor: ")
                result = divide(a, b)
            elif option == "5":
                value = read_float("Value: ")
                use_custom_base = read_text("Custom base? (y/n): ").lower()
                if use_custom_base == "y":
                    base = read_float("Base: ")
                    result = logarithm(value, base)
                else:
                    result = logarithm(value, math.e)
            elif option == "6":
                base = read_float("Base: ")
                exponent = read_float("Exponent: ")
                result = exponential(base, exponent)
            else:
                print("Unknown option. Please choose one from the menu.")
                continue
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Result: {result}")

