class Solution:
    def trailingZeroes(self, n):

        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


sol = Solution()

print(sol.trailingZeroes(3))
print(sol.trailingZeroes(5))
print(sol.trailingZeroes(10))
print(sol.trailingZeroes(25))
print(sol.trailingZeroes(100))