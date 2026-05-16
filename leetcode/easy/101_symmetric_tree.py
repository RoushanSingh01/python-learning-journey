class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        def is_mirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            return (
                left.val == right.val
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)


def run_tests():
    solution = Solution()

    symmetric_root = TreeNode(
        1,
        TreeNode(2, TreeNode(3), TreeNode(4)),
        TreeNode(2, TreeNode(4), TreeNode(3)),
    )

    asymmetric_root = TreeNode(
        1,
        TreeNode(2, None, TreeNode(3)),
        TreeNode(2, None, TreeNode(3)),
    )

    test_cases = [
        (symmetric_root, True),
        (asymmetric_root, False),
    ]

    for index, (root, expected) in enumerate(test_cases, start=1):
        result = solution.isSymmetric(root)

        print(
            f"Test Case {index} | "
            f"Expected: {expected} | "
            f"Got: {result} | "
            f"Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()