class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            result.append([node.val for node in queue])

            queue = [
                child for node in queue for child in (node.left, node.right) if child
            ]

        return result


def run_tests():
    solution = Solution()

    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(20, TreeNode(15), TreeNode(7)),
    )

    result = solution.levelOrder(root)

    print("Expected: [[3], [9, 20], [15, 7]]")
    print("Got     :", result)
    print("Passed  :", result == [[3], [9, 20], [15, 7]])


if __name__ == "__main__":
    run_tests()
