from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []
        visited = set()

        def dfs(row, column, direction):

            visited.add((row, column))
            result.append(matrix[row][column])

            if direction == "r":
                if column + 1 < total_columns and (row, column + 1) not in visited:
                    dfs(row, column + 1, direction)

                elif row + 1 < total_rows and (row + 1, column) not in visited:
                    dfs(row + 1, column, "d")

            elif direction == "d":
                if row + 1 < total_rows and (row + 1, column) not in visited:
                    dfs(row + 1, column, direction)

                elif column and (row, column - 1) not in visited:
                    dfs(row, column - 1, "l")

            elif direction == "l":
                if column and (row, column - 1) not in visited:
                    dfs(row, column - 1, direction)

                elif row and (row - 1, column) not in visited:
                    dfs(row - 1, column, "u")

            else:
                if row and (row - 1, column) not in visited:
                    dfs(row - 1, column, direction)

                elif column + 1 < total_columns and (row, column + 1) not in visited:
                    dfs(row, column + 1, "r")

        if not matrix:
            return []

        total_rows = len(matrix)
        total_columns = len(matrix[0])

        dfs(0, 0, "r")

        return result


def run_test(matrix, expected):
    result = Solution().spiralOrder(matrix)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])

    run_test(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
    )

    run_test([[1]], [1])

    run_test([], [])
