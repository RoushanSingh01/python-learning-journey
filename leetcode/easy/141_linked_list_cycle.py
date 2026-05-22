class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def create_linked_list(values, pos):
    if not values:
        return None

    nodes = [ListNode(val) for val in values]

    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
    ]

    for index, (values, pos) in enumerate(test_cases, start=1):
        head = create_linked_list(values, pos)

        result = solution.hasCycle(head)

        print(f"Test Case {index}")
        print(f"Values: {values}")
        print(f"Cycle Position: {pos}")
        print(f"Has Cycle: {result}")
        print("-" * 40)