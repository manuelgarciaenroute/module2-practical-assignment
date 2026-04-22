"""Console I/O helpers."""

from __future__ import annotations


def read_float(prompt: str) -> float:
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Invalid number. Please try again.")


def read_text(prompt: str) -> str:
    return input(prompt).strip()

