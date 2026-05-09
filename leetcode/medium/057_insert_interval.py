from typing import List


class Solution:

    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int]
    ) -> List[List[int]]:

        merged_intervals = []
        index = 0

        for index, interval in enumerate(intervals):

            if newInterval[1] < interval[0]:

                index -= 1
                break

            elif interval[1] < newInterval[0]:

                merged_intervals += interval,

            else:

                newInterval[0] = min(
                    interval[0],
                    newInterval[0]
                )

                newInterval[1] = max(
                    interval[1],
                    newInterval[1]
                )

        return (
            merged_intervals
            + [newInterval]
            + intervals[index + 1:]
        )


def run_test(intervals, new_interval, expected):

    result = Solution().insert(
        intervals,
        new_interval
    )

    status = (
        "PASS"
        if result == expected
        else "FAIL"
    )

    print(
        f"{status} | expected={expected}, got={result}"
    )


if __name__ == "__main__":

    run_test(
        [[1, 3], [6, 9]],
        [2, 5],
        [[1, 5], [6, 9]]
    )

    run_test(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        [4, 8],
        [[1, 2], [3, 10], [12, 16]]
    )

    run_test(
        [],
        [5, 7],
        [[5, 7]]
    )

    run_test(
        [[1, 5]],
        [2, 3],
        [[1, 5]]
    )

    run_test(
        [[1, 5]],
        [6, 8],
        [[1, 5], [6, 8]]
    )