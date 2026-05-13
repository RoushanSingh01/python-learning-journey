from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        n = len(nums)

        while left <= right:
            while left + 1 < n and nums[left] == nums[left + 1]:
                left += 1

            while right > 0 and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if (
                sum(
                    (
                        target < nums[left],
                        nums[left] <= nums[mid],
                        nums[mid] < target,
                    )
                )
                == 2
            ):
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3),
        ([1, 0, 1, 1, 1], 0),
        ([1, 1, 1, 1, 1], 2),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}")
        print(f"target = {target}")
        print(solution.search(nums, target))
        print("-" * 50)
