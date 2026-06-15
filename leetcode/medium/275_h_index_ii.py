from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        left, right = 0, n

        while left < right:
            mid = (left + right + 1) >> 1

            if citations[n - mid] >= mid:
                left = mid
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [0, 1, 3, 5, 6],
        [1, 2, 100],
        [0],
        [0, 0, 0],
        [11, 15, 20, 25, 30]
    ]

    for citations in test_cases:
        print(f"Input : {citations}")
        print(f"Output: {solution.hIndex(citations)}")
        print()