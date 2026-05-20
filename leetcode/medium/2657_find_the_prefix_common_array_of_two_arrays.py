from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)

        # Since A and B are permutations from 1 to n
        # frequency array is faster than using a set
        freq = [0] * (n + 1)

        ans = [0] * n
        common = 0

        for i in range(n):

            # Process A[i]
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1

            # Process B[i]
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1

            ans[i] = common

        return ans


def run_tests():
    solution = Solution()

    test_cases = [
        {
            "A": [1, 3, 2, 4],
            "B": [3, 1, 2, 4],
            "expected": [0, 2, 3, 4]
        },
        {
            "A": [2, 3, 1],
            "B": [3, 1, 2],
            "expected": [0, 1, 3]
        },
        {
            "A": [1],
            "B": [1],
            "expected": [1]
        },
        {
            "A": [1, 2, 3, 4, 5],
            "B": [5, 4, 3, 2, 1],
            "expected": [0, 0, 1, 3, 5]
        }
    ]

    for i, test in enumerate(test_cases, start=1):

        result = solution.findThePrefixCommonArray(
            test["A"],
            test["B"]
        )

        print(f"Test Case {i}")
        print(f"A        : {test['A']}")
        print(f"B        : {test['B']}")
        print(f"Expected : {test['expected']}")
        print(f"Result   : {result}")

        if result == test["expected"]:
            print("Status   : PASSED")
        else:
            print("Status   : FAILED")

        print("-" * 50)


if __name__ == "__main__":
    run_tests()