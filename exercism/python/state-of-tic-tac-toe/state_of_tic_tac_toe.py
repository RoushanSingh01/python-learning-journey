"""Determine the state of a tic-tac-toe game."""


class InvalidBoardError(ValueError):
    """Raised when a board state is impossible."""


def has_won(board, player):
    """Return True if the player has won."""
    lines = []

    lines.extend(board)

    for column in range(3):
        lines.append(
            "".join(board[row][column] for row in range(3))
        )

    lines.append(
        "".join(board[index][index] for index in range(3))
    )

    lines.append(
        "".join(board[index][2 - index] for index in range(3))
    )

    return any(line == player * 3 for line in lines)


def gamestate(board):
    """Return the state of the tic-tac-toe game."""
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count - o_count > 1:
        raise ValueError("Wrong turn order: X went twice")

    x_wins = has_won(board, "X")
    o_wins = has_won(board, "O")

    if x_wins and o_wins:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins:
        if x_count != o_count + 1:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    if o_wins:
        if x_count != o_count:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    if x_count + o_count == 9:
        return "draw"

    return "ongoing"