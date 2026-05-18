from typing import List


class Solution:
    def getRow(self, row_index: int) -> List[int]:
        row = [1]

        for _ in range(row_index):
            row = [a + b for a, b in zip([0] + row, row + [0])]

        return row


def run_tests():
    solution = Solution()

    assert solution.getRow(0) == [1]

    assert solution.getRow(1) == [1, 1]

    assert solution.getRow(3) == [1, 3, 3, 1]

    assert solution.getRow(5) == [1, 5, 10, 10, 5, 1]

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
