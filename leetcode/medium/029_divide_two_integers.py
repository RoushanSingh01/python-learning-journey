# divide_two_integers.py


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648

        # Edge overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        # Determine sign
        is_negative = (dividend < 0) != (divisor < 0)

        a, b = abs(dividend), abs(divisor)
        quotient = 0

        while a >= b:
            temp_divisor, multiplier = b, 1

            # Find largest shift
            while a >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiplier <<= 1

            a -= temp_divisor
            quotient += multiplier

        result = -quotient if is_negative else quotient

        # Clamp to 32-bit range
        return max(MIN_INT, min(MAX_INT, result))


# ---------- Test Cases ----------


def run_tests():
    solution = Solution()

    test_cases = [
        (10, 3),
        (7, -3),
        (-7, 3),
        (-7, -3),
        (1, 1),
        (0, 1),
        (1, -1),
        (-2147483648, -1),  # overflow case
        (-2147483648, 1),
        (2147483647, 1),
        (100, 5),
        (1024, 2),
        (999, 10),
    ]

    for i, (dividend, divisor) in enumerate(test_cases, start=1):
        result = solution.divide(dividend, divisor)
        expected = int(dividend / divisor)  # for comparison (Python division)

        print(f"\nTest Case {i}:")
        print(f"Input: dividend={dividend}, divisor={divisor}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    run_tests()
