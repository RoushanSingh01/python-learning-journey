from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] != "O"
            ):
                return

            board[r][c] = "S"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)

            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)

            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"


def print_board(board: List[List[str]]) -> None:
    for row in board:
        print(row)
    print()


def run_tests():
    solution = Solution()

    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    solution.solve(board1)

    print("Test Case 1:")
    print_board(board1)

    board2 = [["X"]]

    solution.solve(board2)

    print("Test Case 2:")
    print_board(board2)

    board3 = [
        ["O", "O"],
        ["O", "O"]
    ]

    solution.solve(board3)

    print("Test Case 3:")
    print_board(board3)


if __name__ == "__main__":
    run_tests()