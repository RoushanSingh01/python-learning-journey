class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, target_sum):
        if not root:
            return False

        remaining = target_sum - root.val

        if not root.left and not root.right:
            return remaining == 0

        return (
            self.hasPathSum(root.left, remaining)
            or self.hasPathSum(root.right, remaining)
        )


def run_tests():
    solution = Solution()

    root1 = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                None,
                TreeNode(1)
            )
        )
    )

    assert solution.hasPathSum(root1, 22) is True
    assert solution.hasPathSum(root1, 26) is True
    assert solution.hasPathSum(root1, 18) is True
    assert solution.hasPathSum(root1, 27) is True
    assert solution.hasPathSum(root1, 5) is False
    assert solution.hasPathSum(None, 0) is False

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()