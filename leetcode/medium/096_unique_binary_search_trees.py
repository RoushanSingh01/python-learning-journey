class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(nodes):
                dp[nodes] += dp[root] * dp[nodes - root - 1]

        return dp[n]


def run_tests():
    solution = Solution()

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 14),
        (5, 42),
    ]

    for n, expected in test_cases:
        result = solution.numTrees(n)

        print(
            f"n={n} | Expected={expected} | Got={result} | Passed={result == expected}"
        )


if __name__ == "__main__":
    run_tests()
