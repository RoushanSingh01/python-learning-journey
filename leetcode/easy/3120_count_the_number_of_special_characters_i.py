class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if 'a' <= ch <= 'z':
                lower.add(ch)
            else:
                upper.add(ch)

        return sum(1 for ch in lower if ch.upper() in upper)



sol = Solution()

test_cases = [
    ("aaAbcBC", 3),
    ("abc", 0),
    ("abBCab", 1),
    ("aA", 1),
    ("zZx", 1),
    ("", 0),
]

for word, expected in test_cases:
    result = sol.numberOfSpecialChars(word)
    print(f"Input: {word}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("Passed\n" if result == expected else "Failed\n")