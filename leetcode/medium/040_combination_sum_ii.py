class Solution(object):
    def combinationSum2(self, candidates, target):

        result = []
        candidates.sort()

        def backtrack(candidates, remaining_target, current_combination, index):

            if remaining_target < 0:
                return

            if remaining_target == 0:
                result.append(current_combination)
                return

            previous = -1

            for start in range(index, len(candidates)):

                if previous != candidates[start]:

                    backtrack(
                        candidates,
                        remaining_target - candidates[start],
                        current_combination + [candidates[start]],
                        start + 1
                    )

                    previous = candidates[start]

        backtrack(candidates, target, [], 0)

        return result


def normalize(output):
    return sorted(sorted(combination) for combination in output)


def run_test(candidates, target, expected):
    result = Solution().combinationSum2(candidates, target)

    status = (
        "PASS"
        if normalize(result) == normalize(expected)
        else "FAIL"
    )

    print(
        f"{status} | candidates={candidates}, "
        f"target={target}, got={result}"
    )


if __name__ == "__main__":

    run_test(
        [10, 1, 2, 7, 6, 1, 5],
        8,
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    )

    run_test(
        [2, 5, 2, 1, 2],
        5,
        [[1, 2, 2], [5]]
    )

    run_test(
        [1, 1, 1, 2],
        3,
        [[1, 1, 1], [1, 2]]
    )

    run_test(
        [3, 1, 3, 5, 1, 1],
        8,
        [[1, 1, 1, 5], [1, 1, 3, 3], [3, 5]]
    )