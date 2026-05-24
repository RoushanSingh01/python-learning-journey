from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i]:
                return dp[i]

            best = 1

            # Explore left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            # Explore right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            dp[i] = best
            return best

        return max(dfs(i) for i in range(n))



def run_tests():
    sol = Solution()

    test_cases = [
        {
            "arr": [6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12],
            "d": 2,
            "expected": 4
        },
        {
            "arr": [3, 3, 3, 3, 3],
            "d": 3,
            "expected": 1
        },
        {
            "arr": [7, 6, 5, 4, 3, 2, 1],
            "d": 1,
            "expected": 7
        },
        {
            "arr": [7, 1, 7, 1, 7, 1],
            "d": 2,
            "expected": 2
        },
        {
            "arr": [66],
            "d": 1,
            "expected": 1
        },
    ]

    for idx, test in enumerate(test_cases, 1):
        result = sol.maxJumps(test["arr"], test["d"])

        print(f"Test Case {idx}")
        print(f"Array    : {test['arr']}")
        print(f"d        : {test['d']}")
        print(f"Expected : {test['expected']}")
        print(f"Got      : {result}")
        print("PASS" if result == test["expected"] else "FAIL")
        print("-" * 50)


if __name__ == "__main__":
    run_tests()