# next_permutation.py

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next permutation.
        """
        index_i = len(nums) - 2

        # Step 1: find first decreasing element
        while index_i >= 0 and nums[index_i] >= nums[index_i + 1]:
            index_i -= 1

        # Step 2: swap with next greater element
        if index_i >= 0:
            index_j = len(nums) - 1
            while nums[index_j] <= nums[index_i]:
                index_j -= 1

            nums[index_i], nums[index_j] = nums[index_j], nums[index_i]

        # Step 3: reverse the suffix
        start = index_i + 1
        end = len(nums) - 1

        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# ---------- Test Cases ----------

def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1]),
        ([1], [1]),
        ([1, 3, 2], [2, 1, 3]),
        ([2, 3, 1, 3, 3], [2, 3, 3, 1, 3]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        original = nums[:]
        solution.nextPermutation(nums)

        print(f"\nTest Case {i}")
        print(f"Input:    {original}")
        print(f"Output:   {nums}")
        print(f"Expected: {expected}")
        print("PASS" if nums == expected else "FAIL")


# ---------- Run ----------

if __name__ == "__main__":
    run_tests()