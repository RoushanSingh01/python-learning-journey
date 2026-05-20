from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current: int) -> int:
            if not node:
                return 0

            current = current * 10 + node.val

            if not node.left and not node.right:
                return current

            return dfs(node.left, current) + dfs(node.right, current)

        return dfs(root, 0)


def run_tests():
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(4,
        TreeNode(9, TreeNode(5), TreeNode(1)),
        TreeNode(0)
    )

    solution = Solution()

    print(solution.sumNumbers(root1))  # 25
    print(solution.sumNumbers(root2))  # 1026


if __name__ == "__main__":
    run_tests()