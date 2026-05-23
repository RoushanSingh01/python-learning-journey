from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

                if count > 1:
                    return False

        return True


# ---------------- TEST CASES ---------------- #

def run_tests():
    solution = Solution()

    test_cases = [
        ([3, 4, 5, 1, 2], True),
        ([2, 1, 3, 4], False),
        ([1, 2, 3], True),
        ([1, 1, 1], True),
        ([6, 10, 6], True),
        ([2, 3, 4, 5, 1], True),
        ([5, 1, 2, 3, 4], True),
        ([1, 2, 3, 4, 5], True),
        ([4, 1, 2, 3], True),
        ([3, 5, 1, 2, 4], False),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.check(nums)

        print(f"Test Case {i}")
        print(f"Input    : {nums}")
        print(f"Expected : {expected}")
        print(f"Result   : {result}")
        print(f"Status   : {'PASS' if result == expected else 'FAIL'}")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()