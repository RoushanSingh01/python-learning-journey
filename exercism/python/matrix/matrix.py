"""Matrix row and column access."""


class Matrix:
    """Represent a matrix of integers."""

    def __init__(self, matrix_string):
        """Parse a matrix from a string."""
        self.matrix = [
            [int(value) for value in row.split()]
            for row in matrix_string.splitlines()
        ]

    def row(self, index):
        """Return a row using 1-based indexing."""
        return self.matrix[index - 1]

    def column(self, index):
        """Return a column using 1-based indexing."""
        return [
            row[index - 1]
            for row in self.matrix
        ]