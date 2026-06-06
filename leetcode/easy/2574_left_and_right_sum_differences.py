from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        res = []

        for x in nums:
            res.append(abs(total - 2 * left - x))
            left += x

        return res

if __name__ == "__main__":
    nums = [10, 4, 8, 3]
    print(Solution().leftRightDifference(nums))