class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [i for i in range(n)]

        for center in range(n):
            left = right = center

            while left >= 0 and right < n and s[left] == s[right]:
                cuts = 0 if left == 0 else dp[left - 1] + 1
                dp[right] = min(dp[right], cuts)

                left -= 1
                right += 1

            left, right = center, center + 1

            while left >= 0 and right < n and s[left] == s[right]:
                cuts = 0 if left == 0 else dp[left - 1] + 1
                dp[right] = min(dp[right], cuts)

                left -= 1
                right += 1

        return dp[-1]


def run_tests():
    solution = Solution()

    test_cases = [
        ("aab", 1),
        ("a", 0),
        ("ab", 1),
        ("racecar", 0),
        ("banana", 1)
    ]

    for s, expected in test_cases:
        result = solution.minCut(s)

        print(f"Input: {s}")
        print(f"Expected: {expected}")
        print(f"Output: {result}")
        print()


if __name__ == "__main__":
    run_tests()