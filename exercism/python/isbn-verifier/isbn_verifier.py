def is_valid(isbn):
    pass
"""Utilities for ISBN-10 verification."""


def is_valid(isbn: str) -> bool:
    total = 0
    position = 0

    for char in isbn:
        if char == "-":
            continue

        if char.isdigit():
            value = int(char)
        elif char == "X" and position == 9:
            value = 10
        else:
            return False

        total += value * (10 - position)
        position += 1

    if position != 10:
        return False

    return total % 11 == 0