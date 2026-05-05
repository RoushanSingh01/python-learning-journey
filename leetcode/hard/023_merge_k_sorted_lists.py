# ---------------- LINKED LIST DEFINITION ----------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------------- SOLUTION ----------------
class Solution:
    def mergeKLists(self, lists):
        """
        Improved version:
        - uses heap (optimal)
        - time: O(N log k)
        """
        import heapq

        heap = []

        # push first node of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ---------------- HELPERS ----------------
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def build_lists(list_of_lists):
    return [build_list(lst) for lst in list_of_lists]


def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1]], [1]),
        ([[1, 2, 3], [4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        ([[5, 10], [1, 2, 3], [4, 6, 7, 8]], [1, 2, 3, 4, 5, 6, 7, 8, 10]),
    ]

    for lists, expected in test_cases:
        input_lists = build_lists(lists)
        result = sol.mergeKLists(input_lists)

        print(f"Input: {lists}")
        print(f"Output: {to_list(result)}")
        print(f"Expected: {expected}")

        print("PASS" if to_list(result) == expected else "FAIL")
        print("-" * 60)
