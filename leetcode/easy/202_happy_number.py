class Solution:
    def isHappy(self, n):
        seen = set()

        while n != 1:
            n = sum(int(digit) ** 2 for digit in str(n))

            if n in seen:
                return False

            seen.add(n)

        return True


if __name__ == "__main__":
    sol = Solution()

    test_cases = [19, 2, 7, 20]

    for n in test_cases:
        print(f"{n} -> {sol.isHappy(n)}")