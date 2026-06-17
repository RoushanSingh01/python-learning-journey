from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        k = 0

        for i, x in enumerate(nums):
            if x:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 1],
        [4, 0, 5, 0, 0, 3]
    ]

    for nums in test_cases:
        original = nums[:]
        solution.moveZeroes(nums)

        print(f"Input : {original}")
        print(f"Output: {nums}")
        print()