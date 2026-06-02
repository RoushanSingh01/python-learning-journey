class Solution:
    def rangeBitwiseAnd(self, m, n):
        shifts = 0

        while m != n:
            m >>= 1
            n >>= 1
            shifts += 1

        return m << shifts


def run_tests():
    solution = Solution()

    assert solution.rangeBitwiseAnd(5, 7) == 4
    assert solution.rangeBitwiseAnd(0, 0) == 0
    assert solution.rangeBitwiseAnd(1, 2147483647) == 0
    assert solution.rangeBitwiseAnd(6, 7) == 6

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()