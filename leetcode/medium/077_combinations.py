from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]) -> None:
            if len(path) == k:
                result.append(path[:])
                return

            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()

        backtrack(1, [])

        return result


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (4, 2),
        (1, 1),
        (5, 3),
        (6, 4),
    ]

    for n, k in test_cases:
        print(f"n={n}, k={k}")
        print(solution.combine(n, k))
        print("-" * 40)
