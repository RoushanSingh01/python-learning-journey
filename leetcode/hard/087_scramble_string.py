from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        @lru_cache(None)
        def dfs(a: str, b: str) -> bool:
            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            length = len(a)

            for index in range(1, length):
                if dfs(a[:index], b[:index]) and dfs(a[index:], b[index:]):
                    return True

                if dfs(a[:index], b[-index:]) and dfs(a[index:], b[:-index]):
                    return True

            return False

        return dfs(s1, s2)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("great", "rgeat"),
        ("abcde", "caebd"),
        ("a", "a"),
        ("abc", "bca"),
    ]

    for s1, s2 in test_cases:
        print(f"s1 = {s1}, s2 = {s2}")
        print(solution.isScramble(s1, s2))
        print("-" * 50)
