# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next


# ---------------- TEST CASES ----------------
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


if __name__ == "__main__":
    sol = Solution()

    l1 = create_list([1, 2, 4])
    l2 = create_list([1, 3, 4])

    result = sol.mergeTwoLists(l1, l2)
    print(print_list(result))
