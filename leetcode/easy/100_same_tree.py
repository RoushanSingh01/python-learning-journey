class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


def run_tests():
    solution = Solution()

    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))

    tree3 = TreeNode(1, TreeNode(2))
    tree4 = TreeNode(1, None, TreeNode(2))

    test_cases = [
        (tree1, tree2, True),
        (tree3, tree4, False),
    ]

    for index, (p, q, expected) in enumerate(test_cases, start=1):
        result = solution.isSameTree(p, q)

        print(
            f"Test Case {index} | "
            f"Expected: {expected} | "
            f"Got: {result} | "
            f"Passed: {result == expected}"
        )


if __name__ == "__main__":
    run_tests()
