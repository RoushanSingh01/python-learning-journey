class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # update closest
                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  # exact match

        return closest


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([-1,2,1,-4], 1, 2),
        ([0,0,0], 1, 0),
        ([1,1,1,0], -100, 2),
        ([1,2,5,10,11], 12, 13),
    ]

    for nums, target, expected in test_cases:
        result = sol.threeSumClosest(nums, target)

        print(f"Input: {nums}, target={target}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)