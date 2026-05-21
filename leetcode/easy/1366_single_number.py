class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result


def run_tests():
    solution = Solution()

    test_cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([7, 3, 5, 4, 5, 3, 4], 7)
    ]

    for nums, expected in test_cases:
        result = solution.singleNumber(nums)

        print(f"nums={nums}")
        print(f"expected={expected}, output={result}")
        print()


if __name__ == "__main__":
    run_tests()