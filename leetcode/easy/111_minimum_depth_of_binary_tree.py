class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root):
        return self.compute_depth(root)

    def compute_depth(self, node):
        if not node:
            return 0

        left_depth = self.compute_depth(node.left)
        right_depth = self.compute_depth(node.right)

        if node.left and node.right:
            return min(left_depth, right_depth) + 1

        return max(left_depth, right_depth) + 1


root = TreeNode(
    3,
    TreeNode(9),
    TreeNode(20, TreeNode(15), TreeNode(7))
)

solution = Solution()

print(solution.minDepth(root))