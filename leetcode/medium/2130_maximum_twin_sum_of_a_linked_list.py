class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head):
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next

        return ans


def build_list(arr):
    dummy = ListNode()
    cur = dummy

    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next

    return dummy.next


if __name__ == "__main__":
    head = build_list([5, 4, 2, 1])

    solution = Solution()
    print(solution.pairSum(head))