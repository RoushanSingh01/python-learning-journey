class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder):
        index_map = {
            value: index
            for index, value in enumerate(inorder)
        }

        def dfs(left, right):
            if left > right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = index_map[root_val]

            root.right = dfs(mid + 1, right)
            root.left = dfs(left, mid - 1)

            return root

        return dfs(0, len(inorder) - 1)


def preorder(root):
    if not root:
        return []

    return (
        [root.val]
        + preorder(root.left)
        + preorder(root.right)
    )


solution = Solution()

tree = solution.buildTree(
    [9, 3, 15, 20, 7],
    [9, 15, 7, 20, 3],
)

print(preorder(tree))