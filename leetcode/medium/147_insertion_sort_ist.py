class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(float("-inf"))
        current = head
        prev = dummy

        while current:
            if prev.val > current.val:
                prev = dummy

            while prev.next and prev.next.val < current.val:
                prev = prev.next

            next_node = current.next

            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next


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

    sorted_head = solution.insertionSortList(head)

    print_linked_list(sorted_head)