from collections import defaultdict


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        positions = defaultdict(list)

        for index, char in enumerate(t):
            positions[char].append(index)

        dp = [0] * len(t)

        for char in s:
            if char not in positions:
                continue

            for index in reversed(positions[char]):
                if index == 0:
                    dp[index] += 1
                else:
                    dp[index] += dp[index - 1]

        return dp[-1]


solution = Solution()

print(solution.numDistinct("rabbbit", "rabbit"))
print(solution.numDistinct("babgbag", "bag"))
