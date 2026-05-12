from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3],
        [0],
        [1, 2],
        [4, 5, 6, 7],
    ]

    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Output: {solution.subsets(nums)}")
        print("-" * 50)
