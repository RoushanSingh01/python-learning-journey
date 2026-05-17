class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)


def preorder(root):
    if not root:
        return []

    return [root.val] + preorder(root.left) + preorder(root.right)


solution = Solution()

tree = solution.sortedArrayToBST([-10, -3, 0, 5, 9])

print(preorder(tree))

