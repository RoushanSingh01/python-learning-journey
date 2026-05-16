"""Utilities for formatting resistor labels."""


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

TOLERANCES = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}

UNITS = [
    (1_000_000_000, "gigaohms"),
    (1_000_000, "megaohms"),
    (1_000, "kiloohms"),
    (1, "ohms"),
]


def format_resistance(value):
    """Return formatted resistance with scaled units."""

    for threshold, unit in UNITS:
        if value >= threshold:
            scaled = value / threshold

            if scaled.is_integer():
                scaled = int(scaled)

            return f"{scaled} {unit}"

    return "0 ohms"


def resistor_label(colors):
    """Return formatted resistor specification."""

    if colors == ["black"]:
        return "0 ohms"

    tolerance = TOLERANCES[colors[-1]]

    if len(colors) == 4:
        digits = (
            COLOR_CODES[colors[0]] * 10
            + COLOR_CODES[colors[1]]
        )
        multiplier = COLOR_CODES[colors[2]]

    else:
        digits = (
            COLOR_CODES[colors[0]] * 100
            + COLOR_CODES[colors[1]] * 10
            + COLOR_CODES[colors[2]]
        )
        multiplier = COLOR_CODES[colors[3]]

    resistance = digits * (10 ** multiplier)

    return f"{format_resistance(resistance)} ±{tolerance}"