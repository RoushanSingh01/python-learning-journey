from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1 = len(s1)
        len2 = len(s2)

        if len1 + len2 != len(s3):
            return False

        @cache
        def dfs(i: int, j: int) -> bool:
            k = i + j

            if k == len(s3):
                return True

            if i < len1 and s1[i] == s3[k]:
                if dfs(i + 1, j):
                    return True

            if j < len2 and s2[j] == s3[k]:
                if dfs(i, j + 1):
                    return True

            return False

        return dfs(0, 0)


def run_tests():
    solution = Solution()

    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
        ("", "abc", "abc", True),
        ("abc", "", "abc", True),
    ]

    for s1, s2, s3, expected in test_cases:
        result = solution.isInterleave(s1, s2, s3)

        print(
            f"s1={s1}, s2={s2}, s3={s3}\n"
            f"Expected={expected}, Got={result}, Passed={result == expected}\n"
        )


if __name__ == "__main__":
    run_tests()
