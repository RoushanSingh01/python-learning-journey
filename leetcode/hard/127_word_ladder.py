from collections import deque
import string


class Solution:
    def ladderLength(
        self,
        beginWord,
        endWord,
        wordList
    ):
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    candidate = (
                        word[:i]
                        + char
                        + word[i + 1:]
                    )

                    if candidate in words:
                        words.remove(candidate)

                        queue.append(
                            (candidate, steps + 1)
                        )

        return 0


def run_tests():
    solution = Solution()

    assert solution.ladderLength(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    ) == 5

    assert solution.ladderLength(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"]
    ) == 0

    assert solution.ladderLength(
        "a",
        "c",
        ["a", "b", "c"]
    ) == 2

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()