from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[len(nums) // 2]

        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

        if k <= len(left):
            return self.findKthLargest(left, k)

        if k > len(left) + len(mid):
            return self.findKthLargest(right, k - len(left) - len(mid))

        return pivot


if __name__ == "__main__":
    print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
