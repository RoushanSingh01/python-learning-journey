"""Annotate a flower field with neighboring flower counts."""


def annotate(garden):
    """Return the annotated flower field."""
    if any(
        len(row) != len(garden[0])
        or any(cell not in " *" for cell in row)
        for row in garden
    ):
        raise ValueError("The board is invalid with current input.")

    return [
        _annotated_row(garden, row_index)
        for row_index in range(len(garden))
    ]


def _annotated_row(garden: list[str], row_index: int) -> str:
    """Return a single annotated row."""
    return "".join(
        cell
        if cell == "*"
        else str(_flower_count(garden, row_index, column_index) or " ")
        for column_index, cell in enumerate(garden[row_index])
    )


def _flower_count(
    garden: list[str],
    row_index: int,
    column_index: int,
) -> int:
    """Count neighboring flowers."""
    return sum(
        _is_flower(garden, neighbor_row, neighbor_column)
        for neighbor_row in range(row_index - 1, row_index + 2)
        for neighbor_column in range(column_index - 1, column_index + 2)
    )


def _is_flower(
    garden: list[str],
    row_index: int,
    column_index: int,
) -> int:
    """Return 1 if the position contains a flower, otherwise 0."""
    return int(
        0 <= row_index < len(garden)
        and 0 <= column_index < len(garden[row_index])
        and garden[row_index][column_index] == "*"
    )