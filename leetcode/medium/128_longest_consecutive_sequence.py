from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest


def run_tests():
    solution = Solution()

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
        ([1], 1),
        ([1, 2, 0, 1], 3),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7),
    ]

    for nums, expected in test_cases:
        result = solution.longestConsecutive(nums)
        print(f"nums={nums}")
        print(f"expected={expected}, got={result}")
        print(f"passed={result == expected}\n")


if __name__ == "__main__":
    run_tests()