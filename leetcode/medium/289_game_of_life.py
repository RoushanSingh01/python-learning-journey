from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                live = -board[i][j]

                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n and board[x][y] > 0:
                            live += 1

                if board[i][j] and (live < 2 or live > 3):
                    board[i][j] = 2

                if board[i][j] == 0 and live == 3:
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0],
        ],
        [
            [1, 1],
            [1, 0],
        ],
    ]

    for idx, board in enumerate(test_cases, 1):
        print(f"Test Case {idx}")
        print("Before:")
        for row in board:
            print(row)

        solution.gameOfLife(board)

        print("\nAfter:")
        for row in board:
            print(row)

        print("-" * 30)