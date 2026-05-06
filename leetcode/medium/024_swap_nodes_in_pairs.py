# swap_pairs.py

from typing import Optional, List


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional['ListNode'] = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head.next
        second = head

        second.next = self.swapPairs(first.next)
        first.next = second

        return first


# ---------- Helper Functions ----------

def list_to_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next

    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


def print_linked_list(head: Optional[ListNode]):
    values = linked_list_to_list(head)
    print(" -> ".join(map(str, values)) if values else "Empty List")


# ---------- Test Cases ----------

def run_tests():
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4],
        [],
        [1],
        [1, 2, 3],
        [10, 20, 30, 40, 50],
    ]

    for i, test in enumerate(test_cases, start=1):
        print(f"\nTest Case {i}:")
        head = list_to_linked_list(test)

        print("Input:  ", end="")
        print_linked_list(head)

        swapped = solution.swapPairs(head)

        print("Output: ", end="")
        print_linked_list(swapped)


# ---------- Run ----------

if __name__ == "__main__":
    run_tests()