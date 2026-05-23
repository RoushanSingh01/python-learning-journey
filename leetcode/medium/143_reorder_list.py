class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        if not head:
            return

        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        left, right = 0, len(nodes) - 1

        while left < right:
            nodes[left].next = nodes[right]
            left += 1

            if left == right:
                break

            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None


def create_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    result = []

    while head:
        result.append(str(head.val))
        head = head.next

    print(" -> ".join(result))


if __name__ == "__main__":
    solution = Solution()

    head = create_linked_list([1, 2, 3, 4, 5])

    solution.reorderList(head)

    print_linked_list(head)