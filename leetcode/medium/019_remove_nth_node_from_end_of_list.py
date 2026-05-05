class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        arr = [dummy]

        while head:
            arr.append(head)
            head = head.next

        for _ in range(n + 1):
            pre = arr.pop()

        pre.next = pre.next.next
        return dummy.next


# ---------- HELPERS ----------
def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# ---------- TEST CASES ----------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
    ]

    for arr, n, expected in test_cases:
        head = build_list(arr)
        result = sol.removeNthFromEnd(head, n)

        print(f"Input: {arr}, n={n}")
        print(f"Output: {to_list(result)} | Expected: {expected}")
        print("PASS" if to_list(result) == expected else "FAIL")
        print("-" * 50)
