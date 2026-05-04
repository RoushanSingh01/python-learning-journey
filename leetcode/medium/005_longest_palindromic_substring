class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        res = ""

        for i in range(len(s)):
            # odd length
            temp1 = expand(i, i)
            # even length
            temp2 = expand(i, i + 1)

            if len(temp1) > len(res):
                res = temp1
            if len(temp2) > len(res):
                res = temp2

        return res


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("babad", ["bab", "aba"]),
        ("cbbd", ["bb"]),
        ("a", ["a"]),
        ("ac", ["a", "c"]),
        ("racecar", ["racecar"]),
    ]

    for s, expected in test_cases:
        result = sol.longestPalindrome(s)

        print(f"Input: {s}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result in expected else "FAIL")
        print("-" * 40)
