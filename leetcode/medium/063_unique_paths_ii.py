class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):

                if obstacleGrid[i][j] == 1 or (i == 0 and j == 0):
                    obstacleGrid[i][j] -= 1

                else:
                    add1 = obstacleGrid[i - 1][j] if i > 0 else 0
                    add2 = obstacleGrid[i][j - 1] if j > 0 else 0

                    obstacleGrid[i][j] += add1 + add2

        return abs(obstacleGrid[-1][-1])


def run_test(grid, expected):
    result = Solution().uniquePathsWithObstacles([row[:] for row in grid])

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | grid={grid}")
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Test Cases
run_test(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    2
)

run_test(
    [
        [0, 1],
        [0, 0]
    ],
    1
)

run_test(
    [
        [1]
    ],
    0
)

run_test(
    [
        [0]
    ],
    1
)

run_test(
    [
        [0, 0],
        [1, 1],
        [0, 0]
    ],
    0
)