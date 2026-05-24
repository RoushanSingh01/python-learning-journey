class Solution:
    def maxPoints(self, points):
        m, res, roots = {}, 0, set()

        for i, p1 in enumerate(points):
            if (p1[0], p1[1]) not in roots:
                roots.add((p1[0], p1[1]))

                m.clear()

                dup = path = 0

                for j, p2 in enumerate(points):
                    if i != j:
                        try:
                            cur = (p1[1] - p2[1]) * 100 / (p1[0] - p2[0])

                        except:
                            if p1[1] == p2[1]:
                                dup += 1
                                continue

                            cur = "ver"

                        m[cur] = m.get(cur, 0) + 1

                        if m[cur] > path:
                            path = m[cur]

                if path + dup + 1 > res:
                    res = path + dup + 1

        return res


if __name__ == "__main__":
    solution = Solution()

    points = [[1, 1], [2, 2], [3, 3]]

    result = solution.maxPoints(points)

    print(result)