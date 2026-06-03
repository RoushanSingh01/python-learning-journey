class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        prev, curr = ListNode(None), head

        while curr:
            if curr.val == val:
                if curr == head:
                    head = head.next

                prev.next = curr.next

            if curr.val != val:
                prev = curr

            curr = curr.next

        return head


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for value in values:
        curr.next = ListNode(value)
        curr = curr.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" -> ".join(result) if result else "Empty")


if __name__ == "__main__":
    sol = Solution()

    head = build_linked_list([1, 2, 6, 3, 4, 5, 6])
    val = 6

    result = sol.removeElements(head, val)

    print_linked_list(result)