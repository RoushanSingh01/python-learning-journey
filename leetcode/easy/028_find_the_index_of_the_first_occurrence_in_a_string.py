class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        return -1


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("abc", "c", 2),
    ]

    for haystack, needle, expected in test_cases:
        result = sol.strStr(haystack, needle)

        print(f"Input: {haystack}, {needle}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)
