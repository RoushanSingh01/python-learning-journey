class Solution:
    def minElement(self, nums):
        ans = 100

        for num in nums:
            s = 0
            while num:
                s += num % 10
                num //= 10

            if s < ans:
                ans = s

        return ans


solution = Solution()

test_cases = [
    ([10, 12, 13, 14], 1),
    ([1, 2, 3, 4], 1),
    ([999, 19, 199], 10),
    ([10000], 1),
    ([5555], 20),
    ([9876, 1234], 10),
    ([9999, 8888], 32),
    ([7], 7),
    ([11, 22, 33, 44], 2),
    ([1001, 2002, 3003], 2),
]

for nums, expected in test_cases:
    result = solution.minElement(nums)
    print(
        f"nums = {nums} | Expected = {expected} | Got = {result} | "
        f"{'PASS' if result == expected else 'FAIL'}"
    )