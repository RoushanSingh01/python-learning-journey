class Solution:
    def combinationSum(self, candidates, target):
        result = []
        stack = [(0, [], 0)]
        n = len(candidates)

        while stack:
            current_sum, current_combination, start = stack.pop()

            for index in range(start, n):
                if current_sum + candidates[index] < target:
                    stack.append(
                        (
                            current_sum + candidates[index],
                            current_combination + [candidates[index]],
                            index,
                        )
                    )

                elif current_sum + candidates[index] == target:
                    result.append(current_combination + [candidates[index]])

        return result


def normalize(output):
    return sorted(sorted(comb) for comb in output)


def run_test(candidates, target, expected):
    result = Solution().combinationSum(candidates, target)

    status = "PASS" if normalize(result) == normalize(expected) else "FAIL"

    print(f"{status} | candidates={candidates}, target={target}, got={result}")


if __name__ == "__main__":
    run_test([2, 3, 6, 7], 7, [[2, 2, 3], [7]])

    run_test([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    run_test([2], 1, [])

    run_test([1], 1, [[1]])

    run_test([1], 2, [[1, 1]])
