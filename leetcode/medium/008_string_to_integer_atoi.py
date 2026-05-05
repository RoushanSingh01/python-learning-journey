class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # 1. skip spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # 3. digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # 4. overflow check BEFORE adding
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("42", 42),
        ("   -42", -42),
        ("4193 with words", 4193),
        ("words and 987", 0),
        ("-91283472332", -2147483648),  # overflow
        ("+1", 1),
        ("00000-42a1234", 0),
        ("   +0 123", 0),
    ]

    for s, expected in test_cases:
        result = sol.myAtoi(s)

        print(f"Input: '{s}'")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)