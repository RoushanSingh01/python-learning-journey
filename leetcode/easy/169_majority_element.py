class Solution:
    def majorityElement(self, nums):

        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            count += 1 if num == candidate else -1

        return candidate


sol = Solution()

print(sol.majorityElement([3, 2, 3]))
print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(sol.majorityElement([1]))
print(sol.majorityElement([5, 5, 5, 2, 2]))