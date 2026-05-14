class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next

        for _ in range(right - left):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp

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


def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([3, 5], 1, 2, [5, 3]),
    ]

    for values, left, right, expected in test_cases:
        head = build_linked_list(values)

        result = solution.reverseBetween(head, left, right)

        result_list = linked_list_to_list(result)

        print(
            f"Input: {values}, left={left}, right={right} | "
            f"Expected: {expected} | "
            f"Got: {result_list} | "
            f"Passed: {result_list == expected}"
        )


if __name__ == "__main__":
    run_tests()
