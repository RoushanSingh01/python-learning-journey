from bisect import bisect_left


class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration
    ):

        def prep(start, dur):
            rides = sorted(zip(start, dur))

            s = [x for x, _ in rides]
            n = len(rides)

            pref = [0] * n
            pref[0] = rides[0][1]

            for i in range(1, n):
                pref[i] = min(pref[i - 1], rides[i][1])

            suff = [0] * n
            suff[-1] = rides[-1][0] + rides[-1][1]

            for i in range(n - 2, -1, -1):
                suff[i] = min(suff[i + 1], rides[i][0] + rides[i][1])

            return s, pref, suff

        ws, wp, wf = prep(waterStartTime, waterDuration)
        ls, lp, lf = prep(landStartTime, landDuration)

        ans = float("inf")

        # Land -> Water
        for s, d in zip(landStartTime, landDuration):
            t = s + d
            i = bisect_left(ws, t)

            if i:
                ans = min(ans, t + wp[i - 1])

            if i < len(ws):
                ans = min(ans, wf[i])

        # Water -> Land
        for s, d in zip(waterStartTime, waterDuration):
            t = s + d
            i = bisect_left(ls, t)

            if i:
                ans = min(ans, t + lp[i - 1])

            if i < len(ls):
                ans = min(ans, lf[i])

        return ans


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    print(
        sol.earliestFinishTime(
            [2, 8],
            [4, 1],
            [6],
            [3]
        )
    )  # 9

    # Example 2
    print(
        sol.earliestFinishTime(
            [5],
            [3],
            [1],
            [10]
        )
    )  # 14

    # Additional Test 1
    print(
        sol.earliestFinishTime(
            [1, 5],
            [2, 4],
            [3, 7],
            [3, 1]
        )
    )

    # Additional Test 2
    print(
        sol.earliestFinishTime(
            [10],
            [5],
            [1],
            [2]
        )
    )

    # Additional Test 3
    print(
        sol.earliestFinishTime(
            [1, 2, 3],
            [1, 1, 1],
            [1, 2, 3],
            [1, 1, 1]
        )
    )