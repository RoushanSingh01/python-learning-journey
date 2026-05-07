from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty_cells.append((r, c))
                else:
                    value = board[r][c]
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[(r // 3) * 3 + (c // 3)].add(value)

        def backtrack(index):
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            for value in map(str, range(1, 10)):

                if (
                    value not in rows[r]
                    and value not in cols[c]
                    and value not in boxes[box_index]
                ):

                    board[r][c] = value
                    rows[r].add(value)
                    cols[c].add(value)
                    boxes[box_index].add(value)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(value)
                    cols[c].remove(value)
                    boxes[box_index].remove(value)

            return False

        backtrack(0)


def print_board(board):
    for row in board:
        print(" ".join(row))
    print()


if __name__ == "__main__":

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print("Before Solving:\n")
    print_board(board)

    Solution().solveSudoku(board)

    print("After Solving:\n")
    print_board(board)