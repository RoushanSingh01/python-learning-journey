class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            n *= -1
            x = 1 / x

        elif not n:
            return 1

        half_power = self.myPow(x, n // 2)

        return x * half_power * half_power if n % 2 else half_power * half_power


def run_test(x, n, expected):
    result = Solution().myPow(x, n)

    status = "PASS" if abs(result - expected) < 1e-5 else "FAIL"

    print(f"{status} | x={x}, n={n}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test(2.0, 10, 1024.0)

    run_test(2.1, 3, 9.261)

    run_test(2.0, -2, 0.25)

    run_test(5.0, 0, 1.0)

    run_test(1.0, 100000, 1.0)

    run_test(-2.0, 3, -8.0)
