class Solution:
    def numIslands(self, grid):
        res, n, m = 0, len(grid), len(grid[0]) if grid else 0

        def explore(i, j):
            grid[i][j] = "-1"

            if i > 0 and grid[i - 1][j] == "1":
                explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == "1":
                explore(i, j - 1)
            if i + 1 < n and grid[i + 1][j] == "1":
                explore(i + 1, j)
            if j + 1 < m and grid[i][j + 1] == "1":
                explore(i, j + 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    explore(i, j)
                    res += 1

        return res


def run_tests():
    solution = Solution()

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert solution.numIslands([row[:] for row in grid1]) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert solution.numIslands([row[:] for row in grid2]) == 3

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()