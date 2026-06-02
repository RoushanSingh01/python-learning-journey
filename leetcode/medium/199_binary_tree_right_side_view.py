from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        q, res = [root], []

        while any(q):
            res.append(q[-1].val)
            q = [
                child
                for node in q
                for child in (node.left, node.right)
                if child
            ]

        return res


def run_tests():
    solution = Solution()

    root1 = TreeNode(
        1,
        TreeNode(2, None, TreeNode(5)),
        TreeNode(3, None, TreeNode(4)),
    )
    assert solution.rightSideView(root1) == [1, 3, 4]

    root2 = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3),
    )
    assert solution.rightSideView(root2) == [1, 3]

    root3 = None
    assert solution.rightSideView(root3) == []

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()