from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start: int) -> None:
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()

        dfs(0)
        return result


def run_tests():
    solution = Solution()

    test_cases = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("efe", [["e", "f", "e"], ["efe"]]),
    ]

    for s, expected in test_cases:
        result = solution.partition(s)

        print(f"Input: {s}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print()


if __name__ == "__main__":
    run_tests()