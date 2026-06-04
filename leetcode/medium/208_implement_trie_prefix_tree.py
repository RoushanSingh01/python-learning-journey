class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

if __name__ == "__main__":
    trie = Trie()

    trie.insert("apple")

    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))

    trie.insert("app")

    print(trie.search("app"))