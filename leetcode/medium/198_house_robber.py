class Solution:
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums or [0])

        nums[2] += nums[0]

        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 2], nums[i - 3])

        return max(nums[-1], nums[-2])


def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([1], 1),
        ([], 0),
    ]

    for nums, expected in test_cases:
        result = solution.rob(nums[:])
        assert result == expected, (
            f"Failed: rob({nums}) = {result}, expected {expected}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()