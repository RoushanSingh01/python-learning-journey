class Solution:
    def canJump(self, nums):

        index = 0
        maximum_reach = 0

        while index < len(nums) and index <= maximum_reach:
            if nums[index] + index >= len(nums) - 1:
                return True

            maximum_reach = max(maximum_reach, index + nums[index])

            index += 1

        return False


def run_test(nums, expected):
    result = Solution().canJump(nums)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | nums={nums}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([2, 3, 1, 1, 4], True)

    run_test([3, 2, 1, 0, 4], False)

    run_test([0], True)

    run_test([2, 0, 0], True)

    run_test([1, 0, 1, 0], False)
