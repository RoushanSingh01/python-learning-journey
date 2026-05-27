class Solution:
    def convertToTitle(self, n: int) -> str:

        char = str()

        while n > 0:

            if n % 26 == 0:
                char += "Z"
                n = n // 26 - 1

            else:
                char += chr(n % 26 + ord("@"))
                n = n // 26

        return char[::-1]


sol = Solution()

print(sol.convertToTitle(1))
print(sol.convertToTitle(26))
print(sol.convertToTitle(27))
print(sol.convertToTitle(52))
print(sol.convertToTitle(701))
print(sol.convertToTitle(702))
print(sol.convertToTitle(703))