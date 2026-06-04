"""Find saddle points in a matrix."""


def saddle_points(matrix):
    """Return all saddle points in the matrix."""
    if not matrix:
        return []

    column_count = len(matrix[0])

    for row in matrix:
        if len(row) != column_count:
            raise ValueError("irregular matrix")

    row_maximums = [
        max(row)
        for row in matrix
    ]

    column_minimums = [
        min(
            matrix[row_index][column_index]
            for row_index in range(len(matrix))
        )
        for column_index in range(column_count)
    ]

    points = []

    for row_index, row in enumerate(matrix, start=1):
        for column_index, value in enumerate(row, start=1):
            if (
                value == row_maximums[row_index - 1]
                and value == column_minimums[column_index - 1]
            ):
                points.append(
                    {
                        "row": row_index,
                        "column": column_index,
                    }
                )

    return points