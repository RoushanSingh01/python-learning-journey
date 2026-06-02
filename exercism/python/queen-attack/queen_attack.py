"""Determine whether two queens can attack each other."""


class Queen:
    """Represent a queen on a chessboard."""

    def __init__(self, row, column):
        """Initialize a queen at a valid position."""
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.position = (row, column)

    def can_attack(self, another_queen):
        """Return whether this queen can attack another queen."""
        if self.position == another_queen.position:
            raise ValueError(
                "Invalid queen position: both queens in the same square"
            )

        row1, column1 = self.position
        row2, column2 = another_queen.position

        return (
            row1 == row2
            or column1 == column2
            or abs(row1 - row2) == abs(column1 - column2)
        )