class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False

                if c not in curr.children:
                    return False

                curr = curr.children[c]

            return curr.is_word

        return dfs(0, self.root)

if __name__ == "__main__":
    wd = WordDictionary()

    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    print(wd.search("pad"))   # False
    print(wd.search("bad"))   # True
    print(wd.search(".ad"))   # True
    print(wd.search("b.."))   # True
    print(wd.search("..d"))   # True
    print(wd.search("..."))   # True