class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            prev_value = float("-inf") if mid == 0 else nums[mid - 1]
            next_value = float("-inf") if mid == len(nums) - 1 else nums[mid + 1]

            if prev_value < nums[mid] > next_value:
                return mid

            if prev_value > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [1, 2],
    ]

    for nums in test_cases:
        result = solution.findPeakElement(nums)
        print(f"Array: {nums}")
        print(f"Peak Index: {result}")
        print(f"Peak Value: {nums[result]}")
        print("-" * 40)