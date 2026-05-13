from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(
        self,
        head: Optional[ListNode],
    ) -> Optional[ListNode]:

        if not head:
            return head

        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


def build_linked_list(values):
    dummy = ListNode()
    node = dummy

    for value in values:
        node.next = ListNode(value)
        node = node.next

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
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [1],
        [],
    ]

    for values in test_cases:
        head = build_linked_list(values)
        result = solution.deleteDuplicates(head)

        print(f"Input: {values}")
        print(f"Output: {linked_list_to_list(result)}")
        print("-" * 50)