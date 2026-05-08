class Solution:
    def totalNQueens(self, n):

        total_solutions = [0]

        def dfs(row, left_diagonal, right_diagonal, columns):

            if row == n:
                total_solutions[0] += 1

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

                        dfs(row + 1, left_diagonal, right_diagonal, columns)

                        left_diagonal[column] = 0
                        right_diagonal[column] = 0
                        columns[column] = 0

        dfs(0, [0] * n, [0] * n, [0] * n)

        return total_solutions[0]


def run_test(n, expected):
    result = Solution().totalNQueens(n)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | n={n}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test(1, 1)

    run_test(4, 2)

    run_test(5, 10)

    run_test(6, 4)
