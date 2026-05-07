from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int], result: int = 1) -> int:

        for number in sorted(nums):

            if number == result:
                result += 1

        return result


def run_test(nums, expected):
    result = Solution().firstMissingPositive(nums)

    status = (
        "PASS"
        if result == expected
        else "FAIL"
    )

    print(
        f"{status} | nums={nums}, "
        f"expected={expected}, got={result}"
    )


if __name__ == "__main__":

    run_test([1, 2, 0], 3)

    run_test([3, 4, -1, 1], 2)

    run_test([7, 8, 9, 11, 12], 1)

    run_test([1], 2)

    run_test([2], 1)

    run_test([1, 1], 2)

    run_test([1, 2, 3, 4, 5], 6)