from collections import deque


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return root

        queue = deque([root])

        while queue:
            prev = None

            for _ in range(len(queue)):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root


def collect_levels(root):
    result = []

    while root:
        current = root
        level = []

        while current:
            level.append(current.val)
            current = current.next

        result.append(level)
        root = root.left

    return result


def run_tests():
    solution = Solution()

    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

    solution.connect(root)

    assert collect_levels(root) == [[1], [2, 3], [4, 5, 6, 7]]

    single = Node(1)
    solution.connect(single)

    assert collect_levels(single) == [[1]]

    assert solution.connect(None) is None

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
