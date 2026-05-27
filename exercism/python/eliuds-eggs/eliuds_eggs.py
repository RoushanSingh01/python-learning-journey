"""Module for counting eggs using binary representation."""


def egg_count(display_value):
    """Return the number of eggs represented in binary form."""

    total_eggs = 0

    while display_value > 0:
        total_eggs += display_value & 1
        display_value >>= 1

    return total_eggs