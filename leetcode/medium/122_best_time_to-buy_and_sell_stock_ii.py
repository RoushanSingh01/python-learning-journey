from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -float("inf")
        cash = 0

        for price in prices:
            new_hold = max(hold, cash - price)
            new_cash = max(cash, hold + price)

            hold = new_hold
            cash = new_cash

        return cash


def run_tests():
    solution = Solution()

    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 7

    assert solution.maxProfit([1, 2, 3, 4, 5]) == 4

    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0

    assert solution.maxProfit([1]) == 0

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()