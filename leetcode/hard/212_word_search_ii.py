class Solution:
    def findWords(self, board, words):
        root = {}

        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node["#"] = word

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            c = board[i][j]

            if c not in node:
                return

            nxt = node[c]

            if "#" in nxt:
                res.append(nxt["#"])
                del nxt["#"]

            board[i][j] = "#"

            if i > 0 and board[i - 1][j] != "#":
                dfs(i - 1, j, nxt)
            if i + 1 < m and board[i + 1][j] != "#":
                dfs(i + 1, j, nxt)
            if j > 0 and board[i][j - 1] != "#":
                dfs(i, j - 1, nxt)
            if j + 1 < n and board[i][j + 1] != "#":
                dfs(i, j + 1, nxt)

            board[i][j] = c

            if not nxt:
                node.pop(c)

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res

if __name__ == "__main__":
    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]

    words = ["oath","pea","eat","rain"]

    print(Solution().findWords(board, words))