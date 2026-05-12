from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0

        heights.append(0)

        for index in range(len(heights)):
            while heights[index] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = index - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(index)

        heights.pop()

        return max_area


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [2, 1, 5, 6, 2, 3],
        [2, 4],
        [6, 2, 5, 4, 5, 1, 6],
        [1, 1],
    ]

    for heights in test_cases:
        print(f"Input: {heights}")
        print(f"Largest Area: {solution.largestRectangleArea(heights[:])}")
        print("-" * 50)
