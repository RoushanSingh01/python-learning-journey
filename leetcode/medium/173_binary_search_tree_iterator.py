class TreeNode:
    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):

        stack = []

        while root:
            stack.append(root)
            root = root.left

        self.stack = stack

    def next(self) -> int:

        stack = self.stack

        node = stack.pop()

        current = node.right

        while current:
            stack.append(current)
            current = current.left

        return node.val

    def hasNext(self) -> bool:

        return bool(self.stack)


root = TreeNode(
    7,
    TreeNode(3),
    TreeNode(
        15,
        TreeNode(9),
        TreeNode(20)
    )
)

iterator = BSTIterator(root)

print(iterator.next())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())
print(iterator.next())
print(iterator.hasNext())