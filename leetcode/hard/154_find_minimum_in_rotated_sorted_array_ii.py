class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        result = nums[0]

        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            mid = (left + right) // 2

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1

        return result


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 2, 2, 0, 1]

    result = solution.findMin(nums)

    print(result)