class Solution:
    def setZeroes(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][col] == 0 for col in range(cols))
        first_col_zero = any(matrix[row][0] == 0 for row in range(rows))

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0


def run_test(matrix, expected):
    Solution().setZeroes(matrix)

    if matrix == expected:
        print("PASS")
    else:
        print("FAIL")
        print("Got:")
        for row in matrix:
            print(row)

        print("\nExpected:")
        for row in expected:
            print(row)


if __name__ == "__main__":
    run_test([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]])

    run_test(
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    )

    run_test([[1, 2, 3]], [[1, 2, 3]])

    run_test([[0]], [[0]])
