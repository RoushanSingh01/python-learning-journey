# substring_concat.py

from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)

        if n < total_len:
            return []

        word_map = Counter(words)
        results = []

        for offset in range(word_len):
            left = offset
            right = offset
            curr_map = {}
            matched = 0

            while right + word_len <= n:
                word = s[right:right + word_len]
                right += word_len

                if word in word_map:
                    curr_map[word] = curr_map.get(word, 0) + 1
                    matched += 1

                    # shrink window if excess
                    while curr_map[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        matched -= 1
                        left += word_len

                    if matched == word_count:
                        results.append(left)

                        # slide window forward
                        left_word = s[left:left + word_len]
                        curr_map[left_word] -= 1
                        matched -= 1
                        left += word_len

                else:
                    curr_map.clear()
                    matched = 0
                    left = right

        return results
    


#---------------------TEST CASES-----------------------


def run_tests():
    solution = Solution()

    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("", ["a"], []),
        ("a", [], []),
        ("lingmindraboofooowingdingbarrwingmonkeypoundcake",
         ["fooo", "barr", "wing", "ding", "wing"], [13]),
    ]

    for i, (s, words, expected) in enumerate(test_cases, 1):
        result = solution.findSubstring(s, words)
        print(f"\nTest Case {i}")
        print(f"Input: s={s}, words={words}")
        print(f"Output:   {result}")
        print(f"Expected: {expected}")
        print("PASS" if result == expected else "FAIL")


if __name__ == "__main__":
    run_tests()