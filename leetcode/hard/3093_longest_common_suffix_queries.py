from typing import List


class TrieNode:
    __slots__ = ("child", "idx", "ln")

    def __init__(self):
        self.child = {}
        self.idx = 0
        self.ln = 10**9


class Solution:
    def stringIndices(
        self,
        wordsContainer: List[str],
        wordsQuery: List[str]
    ) -> List[int]:

        root = TrieNode()

        # Build Trie
        for i, word in enumerate(wordsContainer):

            n = len(word)

            node = root

            if n < node.ln:
                node.ln = n
                node.idx = i

            for ch in reversed(word):

                nxt = node.child.get(ch)

                if nxt is None:
                    nxt = TrieNode()
                    node.child[ch] = nxt

                node = nxt

                if n < node.ln:
                    node.ln = n
                    node.idx = i

        ans = []

        # Query
        for word in wordsQuery:

            node = root

            for ch in reversed(word):

                nxt = node.child.get(ch)

                if nxt is None:
                    break

                node = nxt

            ans.append(node.idx)

        return ans



if __name__ == "__main__":

    s = Solution()

    print(
        s.stringIndices(
            ["abcd", "bcd", "xbcd"],
            ["cd", "bcd", "xyz"]
        )
    )
    # [1,1,1]

    print(
        s.stringIndices(
            ["abcdefgh", "poiuygh", "ghghgh"],
            ["gh", "acbfgh", "acbfegh"]
        )
    )
    # [2,0,2]

    print(
        s.stringIndices(
            ["a", "aa", "aaa"],
            ["a", "b", "aa"]
        )
    )
    # [0,0,1]