# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        ret, stack = [], root and [root]

        while stack:
            node = stack.pop()

            ret.append(node.val)

            stack += [
                child
                for child in (node.left, node.right)
                if child
            ]

        return ret[::-1]


def build_tree(values):
    if not values:
        return None

    nodes = [
        TreeNode(val) if val is not None else None
        for val in values
    ]

    kids = nodes[::-1]

    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()

            if kids:
                node.right = kids.pop()

    return root


if __name__ == "__main__":
    solution = Solution()

    root = build_tree([1, None, 2, 3])

    result = solution.postorderTraversal(root)

    print(result)