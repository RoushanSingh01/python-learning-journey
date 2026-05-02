class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):  # take first string as reference
            for j in range(1, len(strs)):
                # stop if mismatch OR string ends
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0]


# ---- test cases ----
s = Solution()

print(s.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
print(s.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
print(s.longestCommonPrefix(["interview", "internet", "internal"]))  # "inte"
print(s.longestCommonPrefix(["a"]))  # "a"
print(s.longestCommonPrefix(["", "b"]))  # ""
