from bisect import bisect_right


class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration,
    ):

        def calc(first_s, first_d, second_s, second_d):
            rides = sorted(range(len(second_s)), key=second_s.__getitem__)

            starts = [0] * len(rides)
            prefix = [0] * len(rides)
            suffix = [0] * len(rides)

            idx = rides[0]
            starts[0] = second_s[idx]
            prefix[0] = second_d[idx]

            for i in range(1, len(rides)):
                idx = rides[i]
                starts[i] = second_s[idx]

                d = second_d[idx]
                prefix[i] = d if d < prefix[i - 1] else prefix[i - 1]

            idx = rides[-1]
            suffix[-1] = second_s[idx] + second_d[idx]

            for i in range(len(rides) - 2, -1, -1):
                idx = rides[i]

                finish = second_s[idx] + second_d[idx]
                suffix[i] = finish if finish < suffix[i + 1] else suffix[i + 1]

            best = 10**18
            n = len(rides)

            for s, d in zip(first_s, first_d):
                finish1 = s + d

                pos = bisect_right(starts, finish1)

                if pos:
                    best = min(best, finish1 + prefix[pos - 1])

                if pos < n:
                    best = min(best, suffix[pos])

            return best

        return min(
            calc(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration,
            ),
            calc(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration,
            ),
        )


if __name__ == "__main__":
    sol = Solution()

    landStartTime = [2, 8]
    landDuration = [4, 1]

    waterStartTime = [6]
    waterDuration = [3]

    result = sol.earliestFinishTime(
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration,
    )

    print("Answer:", result)