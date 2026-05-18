class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, target_sum):
        result = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            if not node.left and not node.right and remaining == 0:
                result.append(path[:])
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            path.pop()

        dfs(root, target_sum)

        return result


def run_tests():
    solution = Solution()

    root = TreeNode(
        5,
        TreeNode(
            4,
            TreeNode(
                11,
                TreeNode(7),
                TreeNode(2)
            )
        ),
        TreeNode(
            8,
            TreeNode(13),
            TreeNode(
                4,
                TreeNode(5),
                TreeNode(1)
            )
        )
    )

    assert solution.pathSum(root, 22) == [
        [5, 4, 11, 2],
        [5, 8, 4, 5]
    ]

    assert solution.pathSum(None, 0) == []

    single = TreeNode(1)
    assert solution.pathSum(single, 1) == [[1]]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()