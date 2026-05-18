class Solution:
    def minimumTotal(self, triangle):
        for row in range(1, len(triangle)):
            current = triangle[row]
            previous = triangle[row - 1]

            for col in range(len(current)):
                if col == 0:
                    current[col] += previous[0]

                elif col == len(current) - 1:
                    current[col] += previous[-1]

                else:
                    current[col] += min(
                        previous[col - 1],
                        previous[col]
                    )

        return min(triangle[-1])


def run_tests():
    solution = Solution()

    triangle1 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]

    assert solution.minimumTotal(triangle1) == 11

    triangle2 = [[-10]]
    assert solution.minimumTotal(triangle2) == -10

    triangle3 = [
        [1],
        [2, 3]
    ]

    assert solution.minimumTotal(triangle3) == 3

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()