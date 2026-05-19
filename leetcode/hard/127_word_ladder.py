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

        begin_set = {beginWord}
        end_set = {endWord}

        steps = 1

        while begin_set and end_set:
            if len(begin_set) > len(end_set):
                begin_set, end_set = (
                    end_set,
                    begin_set
                )

            next_set = set()

            for word in begin_set:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        candidate = (
                            word[:i]
                            + char
                            + word[i + 1:]
                        )

                        if candidate in end_set:
                            return steps + 1

                        if candidate in words:
                            words.remove(candidate)

                            next_set.add(candidate)

            begin_set = next_set

            steps += 1

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