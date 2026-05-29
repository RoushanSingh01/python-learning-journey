from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        return str(int("".join(nums)))


solution = Solution()

test_cases = [
    ([10, 2], "210"),
    ([3, 30, 34, 5, 9], "9534330"),
    ([1], "1"),
    ([10], "10"),
    ([0, 0], "0"),
    ([432, 43243], "43243432"),
]

for nums, expected in test_cases:
    result = solution.largestNumber(nums)

    print(
        f"nums = {nums} | Expected = {expected} | "
        f"Got = {result} | "
        f"{'PASS' if result == expected else 'FAIL'}"
    )
