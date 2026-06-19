class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if (
                char in char_to_word and char_to_word[char] != word
            ) or (
                word in word_to_char and word_to_char[word] != char
            ):
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("abba", "dog cat cat dog"),
        ("abba", "dog cat cat fish"),
        ("aaaa", "dog cat cat dog"),
        ("abba", "dog dog dog dog"),
    ]

    for pattern, s in test_cases:
        print(f"pattern = {pattern}")
        print(f"s       = {s}")
        print(f"output  = {solution.wordPattern(pattern, s)}")
        print()