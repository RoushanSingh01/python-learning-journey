"""Utilities for resistor label generation."""


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


UNITS = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
    (1, "ohms"),
]


def label(colors):
    first = COLOR_CODES[colors[0]]
    second = COLOR_CODES[colors[1]]
    multiplier = COLOR_CODES[colors[2]]

    resistance = (first * 10 + second) * (10 ** multiplier)

    if resistance == 0:
        return "0 ohms"

    for value, unit in UNITS:
        if resistance >= value and resistance % value == 0:
            return f"{resistance // value} {unit}"