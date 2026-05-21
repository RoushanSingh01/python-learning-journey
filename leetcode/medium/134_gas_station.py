class Solution:
    def canCompleteCircuit(self, gas, cost):
        start = 0
        tank = 0
        total = 0

        for i in range(len(gas)):
            balance = gas[i] - cost[i]

            tank += balance
            total += balance

            if tank < 0:
                tank = 0
                start = i + 1

        return start if total >= 0 else -1


def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
        ([5], [4], 0),
        ([3, 1, 1], [1, 2, 2], 0)
    ]

    for gas, cost, expected in test_cases:
        result = solution.canCompleteCircuit(gas, cost)

        print(f"Gas: {gas}")
        print(f"Cost: {cost}")
        print(f"Expected: {expected}")
        print(f"Output: {result}")
        print()


if __name__ == "__main__":
    run_tests()