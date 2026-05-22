import collections


class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        if not head:
            return None

        clones = {None: None}

        current = head

        # First pass: create clone nodes
        while current:
            clones[current] = Node(current.val)
            current = current.next

        current = head

        # Second pass: connect next and random pointers
        while current:
            clones[current].next = clones[current.next]
            clones[current].random = clones[current.random]
            current = current.next

        return clones[head]
    



if __name__ == "__main__":
    n1 = Node(7)
    n2 = Node(13)
    n3 = Node(11)

    n1.next = n2
    n2.next = n3

    n2.random = n1
    n3.random = n1

    copied = Solution().copyRandomList(n1)

    while copied:
        random_val = copied.random.val if copied.random else None
        print(f"Val: {copied.val}, Random: {random_val}")
        copied = copied.next