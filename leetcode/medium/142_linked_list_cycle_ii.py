class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                entry = head

                while entry != slow:
                    entry = entry.next
                    slow = slow.next

                return entry

        return None


def create_cycle_list(values, pos):
    nodes = [ListNode(val) for val in values]

    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


if __name__ == "__main__":
    solution = Solution()

    head = create_cycle_list([3, 2, 0, -4], 1)

    result = solution.detectCycle(head)

    print(result.val if result else None)