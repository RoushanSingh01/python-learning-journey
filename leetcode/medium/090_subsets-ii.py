from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = [[]]
        start = 0

        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                subsets_to_extend = result[start:]
            else:
                subsets_to_extend = result[:]

            start = len(result)

            for subset in subsets_to_extend:
                result.append(subset + [num])

        return result
    


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 2],
        [0],
        [1, 1],
        [4, 4, 4, 1, 4],
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        print(solution.subsetsWithDup(nums))
        print("-" * 50)