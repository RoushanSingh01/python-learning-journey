class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            current = 0

            if s[i] != "0":
                current += prev1

            if "10" <= s[i - 1:i + 1] <= "26":
                current += prev2

            if current == 0:
                return 0

            prev2, prev1 = prev1, current

        return prev1


def run_tests():
    solution = Solution()

    test_cases = [
        ("12", 2),
        ("226", 3),
        ("06", 0),
        ("10", 1),
        ("100", 0),
        ("101", 1),
        ("27", 1),
        ("11106", 2),
    ]

    for s, expected in test_cases:
        result = solution.numDecodings(s)
        print(
            f"Input: {s:<6} Expected: {expected:<2} "
            f"Got: {result:<2} Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()