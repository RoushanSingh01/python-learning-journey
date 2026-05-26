class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def getIntersectionNode(self, headA, headB):
        pointer_a = headA
        pointer_b = headB

        while pointer_a != pointer_b:
            pointer_a = pointer_a.next if pointer_a else headB
            pointer_b = pointer_b.next if pointer_b else headA

        return pointer_a


def build_intersected_lists():
    """
    Creates:

    A: 4 -> 1 \
                  8 -> 4 -> 5
    B:      5 -> 6 -> 1 /
    """

    # Shared part
    shared = ListNode(8)
    shared.next = ListNode(4)
    shared.next.next = ListNode(5)

    # List A
    head_a = ListNode(4)
    head_a.next = ListNode(1)
    head_a.next.next = shared

    # List B
    head_b = ListNode(5)
    head_b.next = ListNode(6)
    head_b.next.next = ListNode(1)
    head_b.next.next.next = shared

    return head_a, head_b


if __name__ == "__main__":
    list_a, list_b = build_intersected_lists()

    solution = Solution()
    intersection = solution.getIntersectionNode(list_a, list_b)

    if intersection:
        print("Intersection Node Value:", intersection.val)
    else:
        print("No intersection found")