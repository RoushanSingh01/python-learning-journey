from math import gcd


class Solution:
    def maxPoints(self, points):
        n = len(points)

        if n <= 2:
            return n

        result = 0

        for i in range(n):
            slopes = {}
            duplicates = 1

            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                g = gcd(dx, dy)

                dx //= g
                dy //= g

                if dx < 0:
                    dx *= -1
                    dy *= -1

                elif dx == 0:
                    dy = 1

                elif dy == 0:
                    dx = 1

                slope = (dx, dy)

                slopes[slope] = slopes.get(slope, 0) + 1

            current_max = duplicates

            for count in slopes.values():
                current_max = max(
                    current_max,
                    count + duplicates
                )

            result = max(result, current_max)

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [[1, 1], [2, 2], [3, 3]],
        [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],
        [[0, 0], [1, 1], [0, 0]],
        [[1, 1], [1, 1], [2, 2], [3, 3]],
    ]

    for points in test_cases:
        print(f"Points: {points}")
        print(f"Max Points on Line: {solution.maxPoints(points)}")
        print("-" * 40)