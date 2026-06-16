from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        path = []

        def dfs(pos: int, prev: int, curr: int):
            if pos == len(num):
                if curr == target:
                    ans.append("".join(path))
                return

            for i in range(pos, len(num)):
                if i > pos and num[pos] == "0":
                    break

                s = num[pos:i + 1]
                val = int(s)

                if pos == 0:
                    path.append(s)
                    dfs(i + 1, val, val)
                    path.pop()
                else:
                    path.extend(["+", s])
                    dfs(i + 1, val, curr + val)
                    path.pop()
                    path.pop()

                    path.extend(["-", s])
                    dfs(i + 1, -val, curr - val)
                    path.pop()
                    path.pop()

                    path.extend(["*", s])
                    dfs(i + 1, prev * val, curr - prev + prev * val)
                    path.pop()
                    path.pop()

        dfs(0, 0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("123", 6),
        ("232", 8),
        ("3456237490", 9191),
        ("105", 5),
    ]

    for num, target in test_cases:
        print(f"num = {num}, target = {target}")
        print(solution.addOperators(num, target))
        print()