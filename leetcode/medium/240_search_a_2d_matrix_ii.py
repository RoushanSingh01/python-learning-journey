class Solution:
    def searchMatrix(self, matrix, target):
        i, j = len(matrix) - 1, 0
        n = len(matrix[0])

        while i >= 0 and j < n:
            x = matrix[i][j]

            if x == target:
                return True

            if x > target:
                i -= 1
            else:
                j += 1

        return False


if __name__ == "__main__":
    solution = Solution()

    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    print(solution.searchMatrix(matrix, 5))
    print(solution.searchMatrix(matrix, 20))