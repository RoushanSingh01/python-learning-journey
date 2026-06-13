from functools import cache
from operator import add, sub, mul


class Solution:
    def diffWaysToCompute(self, expression: str):
        ops = {'+': add, '-': sub, '*': mul}

        @cache
        def dfs(exp):
            if exp.isdigit():
                return [int(exp)]

            ans = []

            for i, c in enumerate(exp):
                if c in ops:
                    left = dfs(exp[:i])
                    right = dfs(exp[i + 1:])

                    op = ops[c]

                    for a in left:
                        for b in right:
                            ans.append(op(a, b))

            return ans

        return dfs(expression)


if __name__ == "__main__":
    expression = "2*3-4*5"

    solution = Solution()
    print(solution.diffWaysToCompute(expression))