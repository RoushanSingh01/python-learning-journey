class Solution:
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2:
            return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell > buy)

        dp = [[0, -float("inf")] for _ in range(k + 1)]

        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]:
                    dp[i][0] = dp[i - 1][1] + p
                if dp[i][0] - p > dp[i][1]:
                    dp[i][1] = dp[i][0] - p

        return dp[-1][0]


if __name__ == "__main__":
    sol = Solution()

    print(sol.maxProfit(2, [2, 4, 1]))                    # 2
    print(sol.maxProfit(2, [3, 2, 6, 5, 0, 3]))          # 7
    print(sol.maxProfit(1, [1, 2]))                      # 1
    print(sol.maxProfit(2, [1, 2, 3, 4, 5]))            # 4
    print(sol.maxProfit(2, [7, 6, 4, 3, 1]))            # 0
    print(sol.maxProfit(3, [1, 3, 2, 8, 4, 9]))         # 13