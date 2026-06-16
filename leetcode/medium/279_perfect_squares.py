from math import isqrt


class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            r = isqrt(x)
            return r * r == x

        if is_square(n):
            return 1

        while n % 4 == 0:
            n //= 4

        if n % 8 == 7:
            return 4

        for i in range(1, isqrt(n) + 1):
            if is_square(n - i * i):
                return 2

        return 3


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        12,
        13,
        1,
        43,
        7168,
    ]

    for n in test_cases:
        print(f"Input : {n}")
        print(f"Output: {solution.numSquares(n)}")
        print()