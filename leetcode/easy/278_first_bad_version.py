def isBadVersion(version: int) -> bool:
    return version >= FIRST_BAD


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = (left + right) >> 1

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    test_cases = [
        (5, 4),
        (1, 1),
        (10, 7),
        (100, 63),
    ]

    solution = Solution()

    for n, first_bad in test_cases:
        FIRST_BAD = first_bad

        print(f"n = {n}, firstBad = {first_bad}")
        print(f"Output: {solution.firstBadVersion(n)}")
        print()