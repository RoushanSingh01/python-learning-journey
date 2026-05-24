class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        values = []

        while head:
            values.append(head.val)
            head = head.next

        values.sort()

        if not values:
            return None

        root = current = ListNode(values[0])

        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next

        return root


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" -> ".join(result))


if __name__ == "__main__":
    solution = Solution()

    head = create_linked_list([4, 2, 1, 3])

    sorted_head = solution.sortList(head)

    print_linked_list(sorted_head)