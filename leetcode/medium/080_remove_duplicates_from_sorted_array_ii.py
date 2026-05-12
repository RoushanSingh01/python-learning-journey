from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        write_index = 2

        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 1],
        [1, 1, 1],
    ]

    for nums in test_cases:
        arr = nums[:]
        k = solution.removeDuplicates(arr)

        print(f"Input: {nums}")
        print(f"k = {k}")
        print(f"Modified array: {arr[:k]}")
        print("-" * 50)
