from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = [0]

        for bit in range(n):
            mask = 1 << bit
            result += [value + mask for value in reversed(result)]

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 2, 3]

    for n in test_cases:
        print(f"n = {n}")
        print(solution.grayCode(n))
        print("-" * 50)
