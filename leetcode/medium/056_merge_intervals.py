class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        res = []

        for start, end in intervals:
            if not res or start > res[-1][1]:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res


# ----------------TEST CASES--------------------


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1,6],[8,10],[15,18]]

print(Solution().merge([[1, 4], [4, 5]]))
# [[1,5]]

print(Solution().merge([[1, 4], [0, 4]]))
# [[0,4]]

print(Solution().merge([[1, 4], [2, 3]]))
# [[1,4]]

print(Solution().merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
# [[1,10]]
