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

        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                duplicate_value = head.val

                while head and head.val == duplicate_value:
                    head = head.next

                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next


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
        [1, 2, 3, 3, 4, 4, 5],
        [1, 1, 1, 2, 3],
        [1, 1],
        [1, 2, 2],
    ]

    for values in test_cases:
        head = build_linked_list(values)
        result = solution.deleteDuplicates(head)

        print(f"Input: {values}")
        print(f"Output: {linked_list_to_list(result)}")
        print("-" * 50)
