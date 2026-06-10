class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                k -= 1

                if k == 0:
                    return root.val

                root = root.right


if __name__ == "__main__":
    root = TreeNode(
        5,
        TreeNode(
            3,
            TreeNode(2, TreeNode(1)),
            TreeNode(4)
        ),
        TreeNode(6)
    )

    solution = Solution()

    print(solution.kthSmallest(root, 3))
    print(solution.kthSmallest(root, 1))
    print(solution.kthSmallest(root, 5))