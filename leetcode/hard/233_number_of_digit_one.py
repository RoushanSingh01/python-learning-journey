from functools import cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        number_str = str(n)
        length = len(number_str)

        @cache
        def dfs(position: int, ones_count: int, limited: bool) -> int:
            if position == length:
                return ones_count

            upper_bound = int(number_str[position]) if limited else 9

            total = 0

            for digit in range(upper_bound + 1):
                total += dfs(
                    position + 1,
                    ones_count + (digit == 1),
                    limited and digit == upper_bound,
                )

            return total

        return dfs(0, 0, True)


if __name__ == "__main__":
    solution = Solution()

    print(solution.countDigitOne(13))
    print(solution.countDigitOne(100))
    print(solution.countDigitOne(1000))