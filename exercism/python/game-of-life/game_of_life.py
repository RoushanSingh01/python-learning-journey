"""Compute the next generation in Conway's Game of Life."""


def count_live_neighbors(matrix, row, column):
    """Return the number of live neighbors around a cell."""
    rows = len(matrix)
    columns = len(matrix[0])
    live_neighbors = 0

    for row_offset in (-1, 0, 1):
        for column_offset in (-1, 0, 1):
            if row_offset == 0 and column_offset == 0:
                continue

            neighbor_row = row + row_offset
            neighbor_column = column + column_offset

            if (
                0 <= neighbor_row < rows
                and 0 <= neighbor_column < columns
            ):
                live_neighbors += matrix[neighbor_row][neighbor_column]

    return live_neighbors


def tick(matrix):
    """Return the next generation of the game board."""
    if not matrix:
        return []

    rows = len(matrix)
    columns = len(matrix[0])

    next_generation = [
        [0] * columns
        for row_number in range(rows)
    ]

    for row in range(rows):
        for column in range(columns):
            neighbors = count_live_neighbors(
                matrix,
                row,
                column,
            )

            if matrix[row][column] == 1:
                if neighbors in {2, 3}:
                    next_generation[row][column] = 1
            elif neighbors == 3:
                next_generation[row][column] = 1

    return next_generation