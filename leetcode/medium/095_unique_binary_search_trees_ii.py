from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []

        @cache
        def dfs(left, right):
            if left > right:
                return [None]

            trees = []

            for root_value in range(left, right + 1):
                left_subtrees = dfs(left, root_value - 1)
                right_subtrees = dfs(root_value + 1, right)

                for left_node in left_subtrees:
                    for right_node in right_subtrees:
                        root = TreeNode(root_value)
                        root.left = left_node
                        root.right = right_node
                        trees.append(root)

            return trees

        return dfs(1, n)


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

    for n in [1, 2, 3]:
        trees = solution.generateTrees(n)

        print(f"n = {n}")
        print(f"Total Trees: {len(trees)}")

        for tree in trees:
            print(serialize(tree))

        print()


if __name__ == "__main__":
    run_tests()
