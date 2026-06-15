class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n

        p2 = p3 = p5 = 0

        for i in range(1, n):
            next2 = dp[p2] * 2
            next3 = dp[p3] * 3
            next5 = dp[p5] * 5

            dp[i] = min(next2, next3, next5)

            if dp[i] == next2:
                p2 += 1

            if dp[i] == next3:
                p3 += 1

            if dp[i] == next5:
                p5 += 1

        return dp[-1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        10,
        1,
        15,
        1690
    ]

    for n in test_cases:
        print(f"n = {n}")
        print(f"nth Ugly Number = {solution.nthUglyNumber(n)}")
        print()