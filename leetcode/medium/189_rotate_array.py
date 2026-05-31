class Solution:
    def rotate(self, nums, k):
        n = k % len(nums)
        nums[:] = nums[-n:] + nums[:-n]


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    sol.rotate(nums, 3)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    sol.rotate(nums, 2)
    print(nums)  # [3, 99, -1, -100]

    nums = [1]
    sol.rotate(nums, 0)
    print(nums)  # [1]

    nums = [1, 2]
    sol.rotate(nums, 3)
    print(nums)  # [2, 1]

    nums = [1, 2, 3]
    sol.rotate(nums, 6)
    print(nums)  # [1, 2, 3]