class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True

            if value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


def run_test(matrix, target, expected):
    result = Solution().searchMatrix(matrix, target)

    if result == expected:
        print(f"PASS | target={target} -> {result}")
    else:
        print(f"FAIL | target={target} -> got {result}, expected {expected}")


if __name__ == "__main__":
    run_test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)

    run_test([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)

    run_test([[1]], 1, True)

    run_test([[1]], 0, False)

    run_test([[1, 3]], 3, True)
