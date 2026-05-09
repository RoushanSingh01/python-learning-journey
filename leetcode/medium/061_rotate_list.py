# 061_rotate_list.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head, k):
        arr, count = [head], 0

        root = last = head

        while last and last.next and count < k:
            last, count = last.next, count + 1
            arr.append(last)

        if k != count:
            k = k % (count + 1)
            last = arr[k]

        if k == 0 or not last:
            return head

        curr = root

        while last.next:
            last, curr = last.next, curr.next

        last.next, curr.next, start = root, None, curr.next

        return start


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


def run_test(values, k, expected):
    head = build_linked_list(values)

    result = Solution().rotateRight(head, k)

    result = linked_list_to_list(result)

    status = "PASS" if result == expected else "FAIL"

    print(f"{status} | values={values}, k={k}")
    print(f"expected={expected}")
    print(f"got     ={result}")
    print()


# Test Cases
run_test([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3])

run_test([0, 1, 2], 4, [2, 0, 1])

run_test([], 3, [])

run_test([1], 0, [1])

run_test([1, 2], 2, [1, 2])