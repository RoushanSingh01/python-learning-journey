class Solution:
    def processStr(self, s: str, k: int) -> str:
        m = 0

        for c in s:
            if c == "*":
                m = max(0, m - 1)
            elif c == "#":
                m <<= 1
            elif c != "%":
                m += 1

        if k >= m:
            return "."

        for c in reversed(s):
            if c == "*":
                m += 1

            elif c == "#":
                m //= 2
                if k >= m:
                    k -= m

            elif c == "%":
                k = m - 1 - k

            else:
                m -= 1
                if k == m:
                    return c

        return "."


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abc", 0),
        ("abc#", 4),
        ("ab%", 0),
        ("a#b%", 2),
        ("abc*", 1),
    ]

    for s, k in test_cases:
        print(f"s = {s}, k = {k}")
        print(f"Output: {solution.processStr(s, k)}")
        print()