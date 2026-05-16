class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = [root]
        result = []
        left_to_right = True

        while queue:
            level = [node.val for node in queue]

            if not left_to_right:
                level.reverse()

            result.append(level)

            queue = [
                child
                for node in queue
                for child in (node.left, node.right)
                if child
            ]

            left_to_right = not left_to_right

        return result


def run_tests():
    solution = Solution()

    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    expected = [[3], [20, 9], [15, 7]]

    result = solution.zigzagLevelOrder(root)

    print("Expected:", expected)
    print("Got     :", result)
    print("Passed  :", result == expected)


if __name__ == "__main__":
    run_tests()