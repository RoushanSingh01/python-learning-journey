class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        inorder_index = {
            value: index
            for index, value in enumerate(inorder)
        }

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            mid = inorder_index[root_value]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)


def serialize(root):
    if not root:
        return None

    return [
        root.val,
        serialize(root.left),
        serialize(root.right),
    ]


def run_tests():
    solution = Solution()

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    root = solution.buildTree(preorder, inorder)

    print(serialize(root))


if __name__ == "__main__":
    run_tests()