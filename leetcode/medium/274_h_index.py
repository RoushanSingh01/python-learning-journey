from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            buckets[min(c, n)] += 1

        papers = 0

        for h in range(n, -1, -1):
            papers += buckets[h]
            if papers >= h:
                return h

        return 0


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [3, 0, 6, 1, 5],
        [1, 3, 1],
        [0],
        [100],
        [11, 15, 7, 8, 9]
    ]

    for citations in test_cases:
        print(f"Input : {citations}")
        print(f"Output: {solution.hIndex(citations)}")
        print()