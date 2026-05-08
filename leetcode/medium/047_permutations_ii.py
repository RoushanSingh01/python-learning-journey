import itertools


class Solution:
    def permuteUnique(self, nums):

        unique_permutations = set()

        for permutation in itertools.permutations(nums):
            if permutation not in unique_permutations:
                unique_permutations.add(permutation)

        return list(unique_permutations)


def normalize(output):
    return sorted([list(permutation) for permutation in output])


def run_test(nums, expected):
    result = Solution().permuteUnique(nums)

    status = "PASS" if normalize(result) == normalize(expected) else "FAIL"

    print(f"{status} | nums={nums}, got={result}")


if __name__ == "__main__":
    run_test([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]])

    run_test(
        [1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )

    run_test([1], [[1]])
