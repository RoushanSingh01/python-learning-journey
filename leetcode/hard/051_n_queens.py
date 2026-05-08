class Solution:
    def solveNQueens(self, n):

        solutions = []

        def dfs(row, left_diagonal, right_diagonal, columns, board):

            if row == n:
                solutions.append(board)

            else:
                left_diagonal = left_diagonal[1:] + [0]
                right_diagonal = [0] + right_diagonal[:-1]

                for column in range(n):
                    if (
                        columns[column]
                        == left_diagonal[column]
                        == right_diagonal[column]
                        == 0
                    ):
                        left_diagonal[column] = 1
                        right_diagonal[column] = 1
                        columns[column] = 1

                        dfs(
                            row + 1,
                            left_diagonal,
                            right_diagonal,
                            columns,
                            board + [("." * column) + "Q" + ("." * (n - column - 1))],
                        )

                        left_diagonal[column] = 0
                        right_diagonal[column] = 0
                        columns[column] = 0

        dfs(0, [0] * n, [0] * n, [0] * n, [])

        return solutions


def normalize(output):
    return sorted([tuple(solution) for solution in output])


def run_test(n, expected):
    result = Solution().solveNQueens(n)

    status = "PASS" if normalize(result) == normalize(expected) else "FAIL"

    print(f"{status} | n={n}, got={result}")


if __name__ == "__main__":
    run_test(4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])

    run_test(1, [["Q"]])
