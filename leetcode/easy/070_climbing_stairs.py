class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first, second = 1, 2

        for _ in range(3, n + 1):
            first, second = second, first + second

        return second


def run_test(n, expected):
    result = Solution().climbStairs(n)

    if result == expected:
        print(f"PASS | n={n} -> {result}")
    else:
        print(f"FAIL | n={n} -> got {result}, expected {expected}")


if __name__ == "__main__":
    run_test(1, 1)
    run_test(2, 2)
    run_test(3, 3)
    run_test(5, 8)
    run_test(10, 89)
    run_test(45, 1836311903)