class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        left, right = 0, x

        while left <= right:
            partitionX = (left + right) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == x else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # correct partition
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                right = partitionX - 1
            else:
                left = partitionX + 1





# -------------------- TEST CASES ----------------

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1,3], [2], 2),
        ([1,2], [3,4], 2.5),
        ([0,0], [0,0], 0),
        ([], [1], 1),
        ([2], [], 2)
    ]

    for nums1, nums2, expected in test_cases:
        result = sol.findMedianSortedArrays(nums1, nums2)

        print(f"Input: {nums1}, {nums2}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)