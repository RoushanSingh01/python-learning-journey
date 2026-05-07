class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif sum((
                target < nums[left],
                nums[left] <= nums[mid],
                nums[mid] < target
            )) == 2:
                left = mid + 1

            else:
                right = mid - 1

        return -1


def run_test(nums, target, expected):
    result = Solution().search(nums, target)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | nums={nums}, target={target}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([4, 5, 6, 7, 0, 1, 2], 0, 4)
    run_test([4, 5, 6, 7, 0, 1, 2], 3, -1)
    run_test([1], 0, -1)
    run_test([1], 1, 0)
    run_test([1, 3], 3, 1)
    run_test([3, 1], 1, 1)
    run_test([5, 1, 3], 5, 0)
    run_test([5, 1, 3], 3, 2)