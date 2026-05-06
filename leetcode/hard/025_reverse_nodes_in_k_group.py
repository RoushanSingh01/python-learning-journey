# reverse_k_group.py

from typing import Optional, List


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head  # important for standalone correctness
        last = dummy

        cur = head
        while cur:
            first, count = cur, 1

            # check if there are k nodes ahead
            while count < k and cur:
                cur = cur.next
                count += 1

            if count == k and cur:
                # reverse k nodes
                cur, prev = first, None
                for _ in range(k):
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt

                # reconnect
                last.next = prev
                last = first
            else:
                last.next = first
                break

        return dummy.next


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
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 2),
        ([1], 2),
        ([], 3),
        ([1, 2, 3, 4, 5, 6], 4),
    ]

    for i, (values, k) in enumerate(test_cases, start=1):
        print(f"\nTest Case {i}: k = {k}")
        head = list_to_linked_list(values)

        print("Input:  ", end="")
        print_linked_list(head)

        result = solution.reverseKGroup(head, k)

        print("Output: ", end="")
        print_linked_list(result)



if __name__ == "__main__":
    run_tests()