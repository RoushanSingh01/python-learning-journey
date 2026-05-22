from collections import defaultdict


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        random_val = self.random.val if self.random else None
        return f"Node(val={self.val}, random={random_val})"


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        clones = defaultdict(lambda: Node(0))

        clones[None] = None
        current = head

        while current:
            clone = clones[current]

            clone.val = current.val
            clone.next = clones[current.next]
            clone.random = clones[current.random]

            current = current.next

        return clones[head]


def print_list(head):
    current = head

    while current:
        random_val = current.random.val if current.random else None
        print(f"Value: {current.val}, Random: {random_val}")
        current = current.next


node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1

copied = Solution().copyRandomList(node1)

print("Original:")
print_list(node1)

print("\nCopied:")
print_list(copied)