class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        def inorder(node):
            if not node:
                return

            yield from inorder(node.left)

            yield node

            yield from inorder(node.right)

        first = None
        second = None
        previous = None

        for node in inorder(root):
            if previous and previous.val > node.val:
                if not first:
                    first = previous

                second = node

            previous = node

        first.val, second.val = second.val, first.val


def inorder_values(node):
    if not node:
        return []

    return inorder_values(node.left) + [node.val] + inorder_values(node.right)


def run_tests():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)

    print("Before:", inorder_values(root))

    solution.recoverTree(root)

    print("After :", inorder_values(root))


if __name__ == "__main__":
    run_tests()
