class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        def dfs(node):
            if node is None:
                return

            path.append(str(node.val))

            if node.left is None and node.right is None:
                ans.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()

        ans = []
        path = []
        dfs(root)

        return ans


if __name__ == "__main__":
    root = TreeNode(
        1,
        TreeNode(2, None, TreeNode(5)),
        TreeNode(3)
    )

    solution = Solution()
    print(solution.binaryTreePaths(root))