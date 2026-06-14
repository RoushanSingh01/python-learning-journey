class Solution:
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else (num - 1) % 9 + 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.addDigits(38))
    print(solution.addDigits(0))
    print(solution.addDigits(99))