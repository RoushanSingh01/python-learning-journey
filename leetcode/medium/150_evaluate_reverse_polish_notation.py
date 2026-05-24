class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))

            else:
                num2, num1 = stack.pop(), stack.pop()

                if token == "+":
                    last = num1 + num2

                elif token == "-":
                    last = num1 - num2

                elif token == "*":
                    last = num1 * num2

                elif token == "/":
                    last = int(num1 / num2)

                stack.append(last)

        return stack[0]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["2", "1", "+", "3", "*"],
        ["4", "13", "5", "/", "+"],
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
    ]

    for tokens in test_cases:
        result = solution.evalRPN(tokens)

        print(f"Tokens: {tokens}")
        print(f"Result: {result}")
        print("-" * 40)