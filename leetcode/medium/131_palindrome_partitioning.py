import unittest
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        if not s:
            return [[]]
            
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

        result = []
        
        def backtrack(start_index: int, current_path: List[str]):
            if start_index == n:
                result.append(current_path[:])
                return

            for end_index in range(start_index, n):
                if dp[start_index][end_index]:
                    current_path.append(s[start_index:end_index + 1])
                    backtrack(end_index + 1, current_path)
                    current_path.pop()

        backtrack(0, [])
        return result


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        self.assertCountEqual(self.solution.partition(s), expected)

    def test_single_character(self):
        s = "a"
        expected = [["a"]]
        self.assertCountEqual(self.solution.partition(s), expected)

    def test_all_same_characters(self):
        s = "ccc"
        expected = [["c", "c", "c"], ["c", "cc"], ["cc", "c"], ["ccc"]]
        self.assertCountEqual(self.solution.partition(s), expected)

if __name__ == '__main__':
    unittest.main()