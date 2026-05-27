class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_last = [-1] * 26
        upper_first = [-1] * 26

        for i, ch in enumerate(word):

            # lowercase
            if 'a' <= ch <= 'z':
                lower_last[ord(ch) - 97] = i

            # uppercase
            else:
                idx = ord(ch) - 65

                # first uppercase occurrence only
                if upper_first[idx] == -1:
                    upper_first[idx] = i

        special = 0

        for i in range(26):
            if (
                lower_last[i] != -1 and
                upper_first[i] != -1 and
                lower_last[i] < upper_first[i]
            ):
                special += 1

        return special


# Test Cases
sol = Solution()

tests = [
    ("aaAbcBC", 3),
    ("abc", 0),
    ("AbBCab", 0),
    ("aA", 1),
    ("Aa", 0),
    ("abcABC", 3),
    ("aabbccAABBCC", 3),
    ("cCceDC", 0),
    ("AbcbDBdD", 1),
]

for word, expected in tests:
    result = sol.numberOfSpecialChars(word)

    print(f"Input: {word}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print(f"Passed: {result == expected}")
    print("-" * 40)