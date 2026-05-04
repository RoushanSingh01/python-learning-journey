class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
    ]

    for s, expected in test_cases:
        result = sol.lengthOfLongestSubstring(s)

        print(f"Input: {s}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)
