from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums):
        xs = reduce(xor, nums)

        a = 0
        diff_bit = xs & -xs

        for x in nums:
            if x & diff_bit:
                a ^= x

        b = xs ^ a

        return [a, b]


if __name__ == "__main__":
    nums = [1, 2, 1, 3, 2, 5]

    solution = Solution()
    print(solution.singleNumber(nums))