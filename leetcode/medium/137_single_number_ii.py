class Solution:
    def singleNumber(self, nums):
        ones = twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones


def run_tests():
    solution = Solution()

    test_cases = [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ([5, 5, 5, 7], 7),
        ([-2, -2, -2, -7], -7)
    ]

    for nums, expected in test_cases:
        result = solution.singleNumber(nums)

        print(f"nums={nums}")
        print(f"expected={expected}, output={result}")
        print()


if __name__ == "__main__":
    run_tests()