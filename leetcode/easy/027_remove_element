class Solution:
    def removeElement(self, nums, val):
        k = 0  # position for next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([3, 2, 2, 3], 3, 2, [2, 2]),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]),
        ([1, 1, 1], 1, 0, []),
        ([4, 5], 3, 2, [4, 5]),
    ]

    for nums, val, expected_k, expected_arr in test_cases:
        arr_copy = nums[:]
        k = sol.removeElement(arr_copy, val)

        print(f"Input: {nums}, val={val}")
        print(f"k = {k}, Expected = {expected_k}")
        print(f"Array = {arr_copy[:k]}, Expected = {expected_arr}")
        print("PASS" if k == expected_k and arr_copy[:k] == expected_arr else "FAIL")
        print("-" * 40)
