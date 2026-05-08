class Solution:
    def jump(self, nums):

        last_reach = 0
        current_reach = 0

        jumps = 0
        index = 0

        while current_reach < len(nums) - 1:
            while index <= last_reach:
                if index + nums[index] > current_reach:
                    current_reach = index + nums[index]

                index += 1

            last_reach = current_reach
            jumps += 1

        return jumps


def run_test(nums, expected):
    result = Solution().jump(nums)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | nums={nums}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([2, 3, 1, 1, 4], 2)

    run_test([2, 3, 0, 1, 4], 2)

    run_test([1, 1, 1, 1], 3)

    run_test([0], 0)

    run_test([1, 2], 1)

    run_test([5, 1, 1, 1, 1, 1], 1)
