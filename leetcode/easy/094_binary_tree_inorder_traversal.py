class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        return result


def run_tests():
    solution = Solution()

    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)

    root2 = None

    root3 = TreeNode(1)

    test_cases = [
        (root1, [1, 3, 2]),
        (root2, []),
        (root3, [1]),
    ]

    for index, (root, expected) in enumerate(test_cases, start=1):
        result = solution.inorderTraversal(root)

        print(
            f"Test Case {index} | "
            f"Expected: {expected} | "
            f"Got: {result} | "
            f"Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()