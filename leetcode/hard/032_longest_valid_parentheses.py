

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices of unmatched parentheses
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # reset base index
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length


# ---------- Test Cases ----------


def run_tests():
    solution = Solution()

    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()", 2),
        ("()(()", 2),
        ("((()))", 6),
        ("()()()", 6),
        ("(()())", 6),
        ("((())())())", 10),
        (")))))))", 0),
        ("(((((((", 0),
    ]

    for i, (s, expected) in enumerate(test_cases, 1):
        result = solution.longestValidParentheses(s)

        print(f"\nTest Case {i}")
        print(f"Input:    {s}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    run_tests()
