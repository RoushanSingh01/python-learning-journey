from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False

if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))