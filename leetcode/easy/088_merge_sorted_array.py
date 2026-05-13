from typing import List


class Solution:
    def merge(
        self,
        nums1: List[int],
        m: int,
        nums2: List[int],
        n: int,
    ) -> None:

        write_index = m + n - 1
        left = m - 1
        right = n - 1

        while left >= 0 and right >= 0:
            if nums1[left] > nums2[right]:
                nums1[write_index] = nums1[left]
                left -= 1
            else:
                nums1[write_index] = nums2[right]
                right -= 1

            write_index -= 1

        nums1[: right + 1] = nums2[: right + 1]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        ([1], 1, [], 0),
        ([0], 0, [1], 1),
    ]

    for nums1, m, nums2, n in test_cases:
        original = nums1[:]

        solution.merge(nums1, m, nums2, n)

        print(f"nums1 = {original}")
        print(f"nums2 = {nums2}")
        print(f"Merged = {nums1}")
        print("-" * 50)
