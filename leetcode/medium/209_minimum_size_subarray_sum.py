class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        curr = 0
        res = len(nums) + 1

        for right, num in enumerate(nums):
            curr += num

            while curr >= target:
                res = min(res, right - left + 1)
                curr -= nums[left]
                left += 1

        return res if res <= len(nums) else 0

if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]

    print(Solution().minSubArrayLen(target, nums))