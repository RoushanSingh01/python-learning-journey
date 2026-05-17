"""Utilities for secret handshake decoding."""


COMMANDS = {
    0: "wink",
    1: "double blink",
    2: "close your eyes",
    3: "jump",
}


def commands(binary_str):
    """Return decoded secret handshake commands."""

    result = []

    reversed_bits = binary_str[::-1]

    for index, bit in enumerate(reversed_bits[:4]):
        if bit == "1":
            result.append(COMMANDS[index])

    if len(reversed_bits) > 4 and reversed_bits[4] == "1":
        result.reverse()

    return result