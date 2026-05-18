from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        if num_rows == 0:
            return []

        triangle = [[1]]

        for _ in range(num_rows - 1):
            prev = triangle[-1]

            triangle.append([1] + [a + b for a, b in zip(prev, prev[1:])] + [1])

        return triangle


def run_tests():
    solution = Solution()

    assert solution.generate(0) == []

    assert solution.generate(1) == [[1]]

    assert solution.generate(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
