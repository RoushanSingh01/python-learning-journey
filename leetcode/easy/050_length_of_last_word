class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1

        # skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        # count last word
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        ("   ", 0),
    ]

    for s, expected in test_cases:
        result = sol.lengthOfLastWord(s)

        print(f"Input: '{s}'")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)