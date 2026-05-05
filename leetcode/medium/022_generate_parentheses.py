from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bfs = [(0, 0, "")]

        for _ in range(n * 2):
            bfs = (
                [(left + 1, right, s + "(") for left, right, s in bfs if left < n] +
                [(left, right + 1, s + ")") for left, right, s in bfs if right < left]
            )

        return [s for _, _, s in bfs]

# ---------------- TEST CASES ----------------
if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (0, [""]),
    ]

    for n, expected in test_cases:
        result = sol.generateParenthesis(n)

        print(f"Input: n={n}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")

        print("PASS" if sorted(result) == sorted(expected) else "FAIL")
        print("-" * 50)