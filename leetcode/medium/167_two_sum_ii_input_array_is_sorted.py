class Solution:
    def twoSum(self, numbers, target):

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum < target:
                left += 1
            else:
                right -= 1


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([2, 3, 4], 6))
print(sol.twoSum([-1, 0], -1))