"""Utilities for resistor color value calculation."""


COLOR_CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list[str]) -> int:
    """Return the resistor value from the first two color bands."""

    first = COLOR_CODES[colors[0]]
    second = COLOR_CODES[colors[1]]

    return first * 10 + second