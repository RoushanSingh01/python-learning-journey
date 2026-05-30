from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)

    def update(self, pos, val):
        pos += self.n
        self.tree[pos] = val

        while pos > 1:
            pos >>= 1
            self.tree[pos] = max(
                self.tree[pos << 1],
                self.tree[pos << 1 | 1]
            )

    def query(self, left, right):
        if left > right:
            return 0

        left += self.n
        right += self.n

        res = 0

        while left <= right:
            if left & 1:
                res = max(res, self.tree[left])
                left += 1

            if not (right & 1):
                res = max(res, self.tree[right])
                right -= 1

            left >>= 1
            right >>= 1

        return res


class Solution:
    def getResults(self, queries):

        max_x = 0
        obstacles = []

        for q in queries:
            max_x = max(max_x, q[1])

            if q[0] == 1:
                obstacles.append(q[1])

        limit = max_x + 1

        sl = SortedList([0, limit])

        for x in obstacles:
            sl.add(x)

        seg = SegmentTree(limit + 2)

        for i in range(1, len(sl)):
            seg.update(sl[i], sl[i] - sl[i - 1])

        ans = []

        bisect_left = sl.bisect_left
        bisect_right = sl.bisect_right
        remove = sl.remove

        for q in reversed(queries):

            if q[0] == 2:

                _, x, sz = q

                idx = bisect_right(x) - 1

                prev_obstacle = sl[idx]

                largest_gap = seg.query(0, x)

                tail_gap = x - prev_obstacle

                ans.append(
                    max(largest_gap, tail_gap) >= sz
                )

            else:

                x = q[1]

                idx = bisect_left(x)

                prev_obstacle = sl[idx - 1]
                next_obstacle = sl[idx + 1]

                seg.update(
                    next_obstacle,
                    next_obstacle - prev_obstacle
                )

                seg.update(x, 0)

                remove(x)

        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (
            [[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]],
            [False, True, True]
        ),
        (
            [[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]],
            [True, True, False]
        ),
        (
            [[2, 5, 5]],
            [True]
        ),
        (
            [[1, 3], [2, 3, 3], [2, 3, 4]],
            [True, False]
        ),
        (
            [[1, 2], [1, 5], [2, 6, 3], [2, 6, 4]],
            [True, False]
        )
    ]

    for i, (queries, expected) in enumerate(test_cases, 1):
        result = sol.getResults(queries)

        print(f"Test Case {i}")
        print("Queries :", queries)
        print("Expected:", expected)
        print("Result  :", result)
        print("PASS" if result == expected else "FAIL")
        print("-" * 50)