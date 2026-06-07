import heapq

class Solution:
    def getSkyline(self, buildings):
        events = sorted(
            [(L, -H, R) for L, R, H in buildings] +
            list({(R, 0, None) for _, R, _ in buildings})
        )

        res = [[0, 0]]
        hp = [(0, float("inf"))]

        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)

            if negH:
                heapq.heappush(hp, (negH, R))

            if res[-1][1] + hp[0][0]:
                res.append([x, -hp[0][0]])

        return res[1:]

if __name__ == "__main__":
    buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings2 = [[0,2,3],[2,5,3]]

    sol = Solution()
    print(sol.getSkyline(buildings1))
    print(sol.getSkyline(buildings2))