from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)

        max_area = 0

        for row in matrix:
            for col in range(cols):
                if row[col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            stack = [-1]

            for index in range(cols + 1):
                while heights[index] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = index - stack[-1] - 1
                    max_area = max(max_area, height * width)

                stack.append(index)

        return max_area


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ],
        [["0"]],
        [["1"]],
        [["1", "1"]],
    ]

    for matrix in test_cases:
        print(solution.maximalRectangle(matrix))
        print("-" * 50)
