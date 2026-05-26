class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pointer_a = headA
        pointer_b = headB

        while pointer_a is not pointer_b:
            pointer_a = headB if pointer_a is None else pointer_a.next
            pointer_b = headA if pointer_b is None else pointer_b.next

        return pointer_a


def create_lists():
    """
    Creates:

    A: 4 -> 1 \
                  8 -> 4 -> 5
    B:      5 -> 6 -> 1 /
    """

    shared = ListNode(8)
    shared.next = ListNode(4)
    shared.next.next = ListNode(5)

    head_a = ListNode(4)
    head_a.next = ListNode(1)
    head_a.next.next = shared

    head_b = ListNode(5)
    head_b.next = ListNode(6)
    head_b.next.next = ListNode(1)
    head_b.next.next.next = shared

    return head_a, head_b


if __name__ == "__main__":
    list_a, list_b = create_lists()

    solution = Solution()
    result = solution.getIntersectionNode(list_a, list_b)

    if result:
        print("Intersection Node:", result.val)
    else:
        print("No intersection found")