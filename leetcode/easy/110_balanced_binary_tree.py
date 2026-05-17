class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        return self.compute_height(root) != -1

    def compute_height(self, node):
        if not node:
            return 0

        left_height = self.compute_height(node.left)

        if left_height == -1:
            return -1

        right_height = self.compute_height(node.right)

        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1


root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

solution = Solution()

print(solution.isBalanced(root))