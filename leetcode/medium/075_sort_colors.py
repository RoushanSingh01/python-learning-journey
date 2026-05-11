class Solution:
    def sortColors(self, nums):
        left = 0
        current = 0
        right = len(nums) - 1

        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1

            elif nums[current] == 1:
                current += 1

            else:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1


def run_test(nums, expected):
    Solution().sortColors(nums)

    if nums == expected:
        print(f"PASS | {nums}")
    else:
        print(f"FAIL | got {nums}, expected {expected}")


if __name__ == "__main__":
    run_test([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    run_test([2, 0, 1], [0, 1, 2])
    run_test([0], [0])
    run_test([1], [1])
    run_test([2, 2, 1, 0, 0, 1], [0, 0, 1, 1, 2, 2])
