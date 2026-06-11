"""Generate a spiral matrix."""

from itertools import cycle


def spiral_matrix(size):
    """Return a size x size matrix filled in spiral order."""
    matrix = [[None] * size for _ in range(size)]

    row, column = 0, 0

    directions = cycle(
        (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        )
    )

    delta_row, delta_column = next(directions)

    for value in range(size**2):
        matrix[row][column] = value + 1

        if (
            not 0 <= row + delta_row < size
            or not 0 <= column + delta_column < size
            or matrix[row + delta_row][column + delta_column] is not None
        ):
            delta_row, delta_column = next(directions)

        row += delta_row
        column += delta_column

    return matrix