class Solution:
    def rotate(self, matrix):

        matrix[:] = [
            [row[index] for row in matrix[::-1]] for index in range(len(matrix))
        ]


def run_test(matrix, expected):
    Solution().rotate(matrix)

    status = "PASS" if matrix == expected else "FAIL"

    print(f"{status} | expected={expected}, got={matrix}")


if __name__ == "__main__":
    run_test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    run_test(
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    )

    run_test([[1]], [[1]])
