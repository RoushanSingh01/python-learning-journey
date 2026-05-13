from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self,
        head: Optional[ListNode],
        x: int,
    ) -> Optional[ListNode]:

        less_dummy = ListNode(-1)
        greater_dummy = ListNode(-1)

        less = less_dummy
        greater = greater_dummy

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next

            head = head.next

        greater.next = None
        less.next = greater_dummy.next

        return less_dummy.next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 4, 3, 2, 5, 2], 3),
        ([2, 1], 2),
        ([1], 0),
    ]

    for values, x in test_cases:
        head = build_linked_list(values)
        result = solution.partition(head, x)

        print(f"Input: {values}, x = {x}")
        print(f"Output: {linked_list_to_list(result)}")
        print("-" * 50)
