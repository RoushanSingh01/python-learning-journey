"""Module for generating a diamond pattern."""


def rows(letter):
    """Return a list representing a diamond for the given letter."""
    
    diamond_size = ord(letter) - ord("A")
    result = []

    for current_index in range(diamond_size + 1):

        outer_spaces = " " * (diamond_size - current_index)
        current_letter = chr(current_index + ord("A"))

        if current_index == 0:
            row = outer_spaces + current_letter + outer_spaces
        else:
            inner_spaces = " " * (2 * current_index - 1)

            row = (
                outer_spaces
                + current_letter
                + inner_spaces
                + current_letter
                + outer_spaces
            )

        result.append(row)

    return result + result[-2::-1]