from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        n1 = len(nums1)
        n2 = len(nums2)

        while i < n1 and j < n2:
            a = nums1[i]
            b = nums2[j]

            if a == b:
                return a

            if a < b:
                i += 1
            else:
                j += 1

        return -1


def run_test(nums1, nums2, expected):
    result = Solution().getCommon(nums1, nums2)

    print(f"nums1 = {nums1}")
    print(f"nums2 = {nums2}")
    print(f"Expected = {expected}")
    print(f"Result   = {result}")
    print("PASS" if result == expected else "FAIL")
    print("-" * 50)


if __name__ == "__main__":
    run_test([1, 2, 3], [2, 4], 2)
    run_test([1, 2, 3, 6], [2, 3, 4, 5], 2)
    run_test([1, 2, 3], [4, 5, 6], -1)
    run_test([1, 1, 2], [1, 3, 4], 1)
    run_test([100, 200, 300], [50, 100, 150], 100)