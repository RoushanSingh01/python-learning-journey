class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        # Maps original node -> copied node
        old_to_new = {None: None}

        current = head

        # First pass:
        # Create all cloned nodes
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass:
        # Connect next and random pointers
        while current:
            copied_node = old_to_new[current]

            copied_node.next = old_to_new[current.next]
            copied_node.random = old_to_new[current.random]

            current = current.next

        return old_to_new[head]


if __name__ == "__main__":
    # Create original list
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)

    n1.next = n2
    n2.next = n3

    n2.random = n1
    n3.random = n1

    # Copy list
    copied_head = Solution().copyRandomList(n1)

    # Print copied list
    current = copied_head

    while current:
        random_val = current.random.val if current.random else None

        print(
            f"Node Value: {current.val}, "
            f"Random Points To: {random_val}"
        )

        current = current.next