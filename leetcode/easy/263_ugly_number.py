class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False

        for x in (2, 3, 5):
            while n % x == 0:
                n //= x

        return n == 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.isUgly(6))
    print(solution.isUgly(14))
    print(solution.isUgly(1))