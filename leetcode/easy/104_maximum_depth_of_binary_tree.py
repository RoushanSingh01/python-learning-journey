class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)


def run_tests():
    solution = Solution()

    root1 = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    root2 = TreeNode(1, None, TreeNode(2))

    test_cases = [
        (root1, 3),
        (root2, 2),
        (None, 0),
    ]

    for index, (root, expected) in enumerate(test_cases, start=1):
        result = solution.maxDepth(root)

        print(
            f"Test Case {index} | "
            f"Expected: {expected} | "
            f"Got: {result} | "
            f"Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()