# 059_spiral_matrix_ii.py


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def dirToIndex(x, y, d):
            if d == "r":
                return (
                    (x, y + 1, d)
                    if y + 1 < n and matrix[x][y + 1] == 0
                    else (x + 1, y, "d")
                )

            elif d == "d":
                return (
                    (x + 1, y, d)
                    if x + 1 < n and matrix[x + 1][y] == 0
                    else (x, y - 1, "l")
                )

            elif d == "l":
                return (
                    (x, y - 1, d)
                    if y > 0 and matrix[x][y - 1] == 0
                    else (x - 1, y, "u")
                )

            return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y + 1, "r")

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        num, direction = 1, "r"
        i = j = 0

        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1

            i, j, direction = dirToIndex(i, j, direction)

        return matrix


def run_test(n, expected):
    result = Solution().generateMatrix(n)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | n={n}")
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Test Cases
run_test(1, [[1]])

run_test(3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])

run_test(4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])
