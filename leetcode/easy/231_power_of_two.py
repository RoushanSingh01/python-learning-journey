class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n == (n & -n)


if __name__ == "__main__":
    solution = Solution()

    print(solution.isPowerOfTwo(1))
    print(solution.isPowerOfTwo(16))
    print(solution.isPowerOfTwo(3))
    print(solution.isPowerOfTwo(0))
    print(solution.isPowerOfTwo(-8))