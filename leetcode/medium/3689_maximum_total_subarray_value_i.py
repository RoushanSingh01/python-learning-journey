from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return k * (max(nums) - min(nums))


if __name__ == "__main__":
    solution = Solution()

    print(solution.maxTotalValue([1, 3, 2], 2))
    print(solution.maxTotalValue([4, 7, 1, 9], 3))