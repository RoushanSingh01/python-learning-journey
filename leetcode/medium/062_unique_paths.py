
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]

        dp[0][0] = 1

        for i in range(n):
            for j in range(m):

                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]

                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]


def run_test(m, n, expected):
    result = Solution().uniquePaths(m, n)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | m={m}, n={n}")
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Test Cases
run_test(3, 7, 28)

run_test(3, 2, 3)

run_test(7, 3, 28)

run_test(3, 3, 6)

run_test(1, 1, 1)