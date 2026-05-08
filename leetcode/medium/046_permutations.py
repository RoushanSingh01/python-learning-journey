import itertools


class Solution:
    def permute(self, nums):
        return list(itertools.permutations(nums))


def normalize(output):
    return sorted([list(permutation) for permutation in output])


def run_test(nums, expected):
    result = Solution().permute(nums)

    status = "PASS" if normalize(result) == normalize(expected) else "FAIL"

    print(f"{status} | nums={nums}, got={result}")


if __name__ == "__main__":
    run_test(
        [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    run_test([0, 1], [[0, 1], [1, 0]])

    run_test([1], [[1]])
