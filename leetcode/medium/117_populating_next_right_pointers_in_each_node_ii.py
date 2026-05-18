class Node:
    def __init__(
        self,
        val=0,
        left=None,
        right=None,
        next=None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        head = root
        dummy = Node(0)

        while head:
            tail = dummy
            current = head

            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next

                if current.right:
                    tail.next = current.right
                    tail = tail.next

                current = current.next

            head = dummy.next
            dummy.next = None

        return root


def collect_levels(root):
    result = []

    while root:
        current = root
        level = []
        next_level = None

        while current:
            level.append(current.val)

            if not next_level:
                next_level = current.left or current.right

            current = current.next

        result.append(level)
        root = next_level

    return result


def run_tests():
    solution = Solution()

    root = Node(
        1,
        Node(2, Node(4), Node(5)),
        Node(3, None, Node(7))
    )

    solution.connect(root)

    assert collect_levels(root) == [
        [1],
        [2, 3],
        [4, 5, 7]
    ]

    single = Node(1)
    solution.connect(single)

    assert collect_levels(single) == [[1]]

    assert solution.connect(None) is None

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()