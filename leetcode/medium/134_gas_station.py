class Solution:
    def canCompleteCircuit(self, gas, cost):
        cur = total = start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            cur += diff
            total += diff

            if cur < 0:
                cur = 0
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

        print(f"gas={gas}")
        print(f"cost={cost}")
        print(f"expected={expected}, output={result}")
        print()


if __name__ == "__main__":
    run_tests()