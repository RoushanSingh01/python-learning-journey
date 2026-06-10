"""Determine the winner of a Connect game."""


class ConnectGame:
    """Represent a Connect game board."""

    def __init__(self, board):
        self.board = [
            [stone for stone in row]
            for row in board.replace(" ", "").splitlines()
        ]

        self.neighbours = [
            (0, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, 0),
            (-1, 1),
        ]

    def get_winner(self):
        """Return the winning player or an empty string."""
        for player in ("O", "X"):
            if self.checker(player):
                return player

        return ""

    def checker(self, player):
        """Check whether a player has a winning path."""
        if player == "O":
            array = self.board
        elif player == "X":
            array = list(zip(*self.board))
        else:
            return False

        stones = [
            (index, 0)
            for index, stone in enumerate(array[0])
            if stone == player
        ]

        ends = [
            (index, len(array) - 1)
            for index, stone in enumerate(array[-1])
            if stone == player
        ]

        for stone in stones:
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                col = stone[0] + neighbour[0]

                if row >= 0 and col >= 0:
                    try:
                        if (
                            array[row][col] == player
                            and (col, row) not in stones
                        ):
                            stones.append((col, row))
                    except IndexError:
                        continue

        for end in ends:
            if end in stones:
                return True

        return False