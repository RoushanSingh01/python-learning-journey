class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []

        n = len(nums)

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        # skip duplicates
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0,
         [[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]),

        ([2,2,2,2,2], 8,
         [[2,2,2,2]]),

        ([1,2,3,4], 100, []),

        ([-3,-1,0,2,4,5], 2,
         [[-3,-1,2,4]]),

        ([0,0,0,0], 0,
         [[0,0,0,0]]),
    ]

    for nums, target, expected in test_cases:
        result = sol.fourSum(nums, target)

        print(f"Input: nums={nums}, target={target}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")

        res_sorted = sorted([sorted(x) for x in result])
        exp_sorted = sorted([sorted(x) for x in expected])

        print("PASS" if res_sorted == exp_sorted else "FAIL")
        print("-" * 50)