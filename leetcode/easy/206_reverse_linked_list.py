class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode, pre=None) -> ListNode:
        if head:
            nex = head.next
            head.next = pre
            return self.reverseList(nex, head) if nex else head
        return None

def build(nums):
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    head = build([1, 2, 3, 4, 5])
    ans = Solution().reverseList(head)
    print_list(ans)