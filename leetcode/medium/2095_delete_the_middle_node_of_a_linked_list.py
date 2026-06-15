from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow, fast = dummy, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next

        return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    curr = dummy

    for val in values:
        curr.next = ListNode(val)
        curr = curr.next

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
        [1, 3, 4, 7, 1, 2, 6],
        [1, 2, 3, 4],
        [2, 1],
        [1]
    ]

    for i, test in enumerate(test_cases, start=1):
        head = build_linked_list(test)
        result = solution.deleteMiddle(head)
        print(f"Test Case {i}:")
        print(f"Input : {test}")
        print(f"Output: {linked_list_to_list(result)}")
        print()