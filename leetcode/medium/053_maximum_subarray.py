class Solution:
    def maxSubArray(self, nums):

        current_sum = 0
        minimum_prefix_sum = 0

        maximum_subarray_sum = -float("inf")

        for number in nums:
            current_sum += number

            maximum_subarray_sum = max(
                maximum_subarray_sum, current_sum - minimum_prefix_sum
            )

            minimum_prefix_sum = min(minimum_prefix_sum, current_sum)

        return maximum_subarray_sum


def run_test(nums, expected):
    result = Solution().maxSubArray(nums)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | nums={nums}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)

    run_test([1], 1)

    run_test([5, 4, -1, 7, 8], 23)

    run_test([-1, -2, -3], -1)

    run_test([0, 0, 0], 0)
