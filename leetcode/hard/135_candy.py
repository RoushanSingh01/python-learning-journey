class Solution:
    def candy(self, ratings):
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1

        return sum(candies)


def run_tests():
    solution = Solution()

    test_cases = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1, 3, 4, 5, 2], 11),
        ([1, 2, 87, 87, 87, 2, 1], 13)
    ]

    for ratings, expected in test_cases:
        result = solution.candy(ratings)

        print(f"ratings={ratings}")
        print(f"expected={expected}, output={result}")
        print()


if __name__ == "__main__":
    run_tests()