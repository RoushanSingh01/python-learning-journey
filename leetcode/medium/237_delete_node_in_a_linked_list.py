class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    print("Before:")
    print_list(head)

    node_to_delete = head.next

    Solution().deleteNode(node_to_delete)

    print("After:")
    print_list(head)