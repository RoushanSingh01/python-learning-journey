class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # position for next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([], 0, []),
    ]

    for nums, expected_k, expected_arr in test_cases:
        arr_copy = nums[:]  # avoid modifying original test case
        k = sol.removeDuplicates(arr_copy)

        print(f"Input: {nums}")
        print(f"k = {k}, Expected = {expected_k}")
        print(f"Array = {arr_copy[:k]}, Expected = {expected_arr}")
        print("PASS" if k == expected_k and arr_copy[:k] == expected_arr else "FAIL")
        print("-" * 40)
