class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        current = slow

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


if __name__ == "__main__":
    head1 = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    head2 = ListNode(1, ListNode(2))
    head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))

    solution = Solution()

    print(solution.isPalindrome(head1))
    print(solution.isPalindrome(head2))
    print(solution.isPalindrome(head3))