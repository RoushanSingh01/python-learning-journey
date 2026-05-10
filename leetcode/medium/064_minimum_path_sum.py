class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):

                if i == 0 and j == 0:
                    continue

                top = grid[i - 1][j] if i > 0 else float("inf")
                left = grid[i][j - 1] if j > 0 else float("inf")

                grid[i][j] += min(top, left)

        return grid[-1][-1]


def run_test(grid, expected):
    result = Solution().minPathSum([row[:] for row in grid])

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | expected={expected}, got={result}")


# Test Cases
run_test(
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ],
    7
)

run_test(
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    12
)

run_test(
    [
        [5]
    ],
    5
)

run_test(
    [
        [1, 2],
        [1, 1]
    ],
    3
)