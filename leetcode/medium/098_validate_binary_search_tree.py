class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root):
        def validate(node, lower, upper):
            if not node:
                return True

            if not (lower < node.val < upper):
                return False

            return (
                validate(node.left, lower, node.val)
                and validate(node.right, node.val, upper)
            )

        return validate(root, float("-inf"), float("inf"))


def run_tests():
    solution = Solution()

    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    test_cases = [
        (root1, True),
        (root2, False),
    ]

    for index, (root, expected) in enumerate(test_cases, start=1):
        result = solution.isValidBST(root)

        print(
            f"Test Case {index} | "
            f"Expected: {expected} | "
            f"Got: {result} | "
            f"Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()