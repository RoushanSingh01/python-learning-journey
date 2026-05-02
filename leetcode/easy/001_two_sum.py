class Solution:
    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i


# ---- test cases ----
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))  # expected [0,1]
print(s.twoSum([3, 2, 4], 6))  # expected [1,2]
print(s.twoSum([3, 3], 6))  # expected [0,1]
