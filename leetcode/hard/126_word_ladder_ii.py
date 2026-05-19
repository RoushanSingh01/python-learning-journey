from collections import defaultdict
import string


class Solution:
    def findLadders(
        self,
        beginWord,
        endWord,
        wordList
    ):
        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)

        layer = {beginWord}

        found = False

        while layer and not found:
            next_layer = set()

            for word in layer:
                words.discard(word)

            for word in layer:
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        candidate = (
                            word[:i]
                            + char
                            + word[i + 1:]
                        )

                        if candidate in words:
                            parents[candidate].append(word)

                            next_layer.add(candidate)

                            if candidate == endWord:
                                found = True

            layer = next_layer

        if not found:
            return []

        result = []

        def backtrack(word, path):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                backtrack(
                    parent,
                    path + [parent]
                )

        backtrack(endWord, [endWord])

        return result


def run_tests():
    solution = Solution()

    result1 = solution.findLadders(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log", "cog"]
    )

    expected1 = sorted([
        ["hit", "hot", "dot", "dog", "cog"],
        ["hit", "hot", "lot", "log", "cog"]
    ])

    assert sorted(result1) == expected1

    result2 = solution.findLadders(
        "hit",
        "cog",
        ["hot", "dot", "dog", "lot", "log"]
    )

    assert result2 == []

    result3 = solution.findLadders(
        "a",
        "c",
        ["a", "b", "c"]
    )

    expected3 = [["a", "c"]]

    assert result3 == expected3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()