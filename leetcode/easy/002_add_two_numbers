# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# ---------------- TEST HELPERS ----------------
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next


def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9], [1], [0, 0, 0, 1]),
    ]

    for l1_arr, l2_arr, expected in test_cases:
        l1 = create_list(l1_arr)
        l2 = create_list(l2_arr)

        result = sol.addTwoNumbers(l1, l2)
        output = print_list(result)

        print(f"Input: {l1_arr}, {l2_arr}")
        print(f"Output: {output} | Expected: {expected}")
        print("PASS" if output == expected else "FAIL")
        print("-" * 40)
