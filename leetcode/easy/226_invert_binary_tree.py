from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None

        left_subtree = self.invertTree(root.left)
        right_subtree = self.invertTree(root.right)

        root.left, root.right = right_subtree, left_subtree

        return root


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

    return result


if __name__ == "__main__":
    root = TreeNode(
        4,
        TreeNode(
            2,
            TreeNode(1),
            TreeNode(3)
        ),
        TreeNode(
            7,
            TreeNode(6),
            TreeNode(9)
        )
    )

    solution = Solution()

    inverted = solution.invertTree(root)

    print(level_order(inverted))