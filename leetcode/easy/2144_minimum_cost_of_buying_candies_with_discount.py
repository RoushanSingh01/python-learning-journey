from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        ans = 0
        for i in range(0, len(cost), 3):
            ans += cost[i]
            if i + 1 < len(cost):
                ans += cost[i + 1]

        return ans


def run_tests():
    sol = Solution()

    test_cases = [
        ([1, 2, 3], 5),
        ([6, 5, 7, 9, 2, 2], 23),
        ([5, 5], 10),
        ([5], 5),
        ([1, 2, 3, 4, 5, 6], 16),
        ([10, 9, 8, 7, 6, 5, 4], 35),
    ]

    for cost, expected in test_cases:
        result = sol.minimumCost(cost[:])
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: cost={cost}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_tests()