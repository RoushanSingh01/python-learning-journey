class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        best = -float("inf")

        def dfs(node):
            nonlocal best

            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            best = max(
                best,
                node.val + left + right
            )

            return node.val + max(left, right)

        dfs(root)

        return best


def run_tests():
    solution = Solution()

    root1 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )

    assert solution.maxPathSum(root1) == 6

    root2 = TreeNode(
        -10,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )

    assert solution.maxPathSum(root2) == 42

    root3 = TreeNode(-3)

    assert solution.maxPathSum(root3) == -3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()