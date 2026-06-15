from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n + 1) * n // 2 - sum(nums)


if __name__ == "__main__":
    solution = Solution()


    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
    ]

    for nums in test_cases:
        print(f"Input : {nums}")
        print(f"Output: {solution.missingNumber(nums)}")
        print()
