from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(accumulate(gain, initial=0))


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [-5, 1, 5, 0, -7],
        [-4, -3, -2, -1, 4, 3, 2],
        [1, 2, 3],
        [-1, -2, -3],
    ]

    for gain in test_cases:
        print(f"gain   = {gain}")
        print(f"output = {solution.largestAltitude(gain)}")
        print()