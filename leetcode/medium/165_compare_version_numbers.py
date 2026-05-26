class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = j = 0
        n1, n2 = len(version1), len(version2)

        while i < n1 or j < n2:
            num1 = 0
            num2 = 0

            while i < n1 and version1[i] != '.':
                num1 = num1 * 10 + ord(version1[i]) - 48
                i += 1

            while j < n2 and version2[j] != '.':
                num2 = num2 * 10 + ord(version2[j]) - 48
                j += 1

            if num1 > num2:
                return 1

            if num1 < num2:
                return -1

            i += 1
            j += 1

        return 0


# Test Cases
sol = Solution()

print(sol.compareVersion("1.2", "1.10"))      # -1
print(sol.compareVersion("1.01", "1.001"))    # 0
print(sol.compareVersion("1.0", "1.0.0"))     # 0
print(sol.compareVersion("0.1", "1.1"))       # -1
print(sol.compareVersion("1.2.3", "1.2.3"))   # 0