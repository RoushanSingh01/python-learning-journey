class Solution:
    def titleToNumber(self, s):

        return sum((ord(char) - 64) * (26**index) for index, char in enumerate(s[::-1]))


sol = Solution()

print(sol.titleToNumber("A"))
print(sol.titleToNumber("AB"))
print(sol.titleToNumber("ZY"))
print(sol.titleToNumber("FXSHRXW"))
