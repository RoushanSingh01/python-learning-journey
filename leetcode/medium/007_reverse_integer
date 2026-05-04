class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2**31
        MAX = 2**31 - 1

        sign = 1 if x >= 0 else -1
        x = abs(x)

        rev = int(str(x)[::-1])
        rev *= sign

        if rev < MIN or rev > MAX:
            return 0

        return rev


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),     # overflow
        (-1563847412, 0),    # tricky failing case you saw
        (1463847412, 2147483641),
    ]

    for x, expected in test_cases:
        result = sol.reverse(x)

        print(f"Input: {x}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)