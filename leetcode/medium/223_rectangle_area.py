class Solution:
    def computeArea(self, a, b, c, d, e, f, g, h):
        area1 = abs(a - c) * abs(b - d)
        area2 = abs(e - g) * abs(f - h)

        overlap_width = max(a, c, e, g) - min(a, c, e, g)
        overlap_height = max(b, d, f, h) - min(b, d, f, h)

        if overlap_width < abs(a - c) + abs(e - g) and overlap_height < abs(b - d) + abs(f - h):
            intersection = (abs(a - c) + abs(e - g) - overlap_width) * (
                abs(b - d) + abs(f - h) - overlap_height
            )
        else:
            intersection = 0

        return area1 + area2 - intersection


if __name__ == "__main__":
    solution = Solution()

    print(solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
    print(solution.computeArea(-2, -2, 2, 2, -2, -2, 2, 2))