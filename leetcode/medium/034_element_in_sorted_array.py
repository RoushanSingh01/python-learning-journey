import bisect


class Solution(object):
    def searchRange(self, nums, target):
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        return [left, right] if 0 <= left <= right else [-1, -1]


def run_test(nums, target, expected):
    result = Solution().searchRange(nums, target)
    status = "PASS" if result == expected else "FAIL"
    print(f"{status} | nums={nums}, target={target}, expected={expected}, got={result}")


if __name__ == "__main__":
    run_test([5, 7, 7, 8, 8, 10], 8, [3, 4])
    run_test([5, 7, 7, 8, 8, 10], 6, [-1, -1])
    run_test([], 0, [-1, -1])
    run_test([1], 1, [0, 0])
    run_test([1], 0, [-1, -1])
    run_test([2, 2], 2, [0, 1])
    run_test([1, 2, 3, 3, 3, 4], 3, [2, 4])