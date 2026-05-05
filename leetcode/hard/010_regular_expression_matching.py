class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            # if pattern ends
            if j == len(p):
                return i == len(s)

            # check first match
            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # handle *
            if j + 1 < len(p) and p[j + 1] == "*":
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                result = first_match and dfs(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return dfs(0, 0)


# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("abc", "a.c", True),
        ("aaa", "ab*a*c*a", True),
    ]

    for s, p, expected in test_cases:
        result = sol.isMatch(s, p)

        print(f"s = {s}, p = {p}")
        print(f"Output: {result} | Expected: {expected}")
        print("PASS" if result == expected else "FAIL")
        print("-" * 40)
