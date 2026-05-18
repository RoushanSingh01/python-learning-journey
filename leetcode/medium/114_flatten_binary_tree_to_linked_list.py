class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        def dfs(node):
            if not node:
                return None

            left_tail = dfs(node.left)
            right_tail = dfs(node.right)

            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            if right_tail:
                return right_tail

            if left_tail:
                return left_tail

            return node

        dfs(root)


def linked_list_values(root):
    values = []

    while root:
        values.append(root.val)

        if root.left:
            raise AssertionError("Left child should be None")

        root = root.right

    return values


def run_tests():
    solution = Solution()

    root = TreeNode(
        1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6))
    )

    solution.flatten(root)

    assert linked_list_values(root) == [1, 2, 3, 4, 5, 6]

    single = TreeNode(1)
    solution.flatten(single)
    assert linked_list_values(single) == [1]

    solution.flatten(None)

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
