class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            delta = prices[i] - prices[i - 1]

            current_profit = max(0, current_profit + delta)

            max_profit = max(max_profit, current_profit)

        return max_profit


def run_tests():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0

    assert solution.maxProfit([1, 2]) == 1

    assert solution.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2

    assert solution.maxProfit([1]) == 0

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
