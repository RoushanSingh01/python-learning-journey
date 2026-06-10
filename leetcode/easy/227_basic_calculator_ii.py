class Solution:
    def calculate(self, s: str) -> int:
        value = 0
        sign = "+"
        stack = []
        length = len(s)

        for index, char in enumerate(s):
            if char.isdigit():
                value = value * 10 + int(char)

            if index == length - 1 or char in "+-*/":
                match sign:
                    case "+":
                        stack.append(value)
                    case "-":
                        stack.append(-value)
                    case "*":
                        stack.append(stack.pop() * value)
                    case "/":
                        stack.append(int(stack.pop() / value))

                sign = char
                value = 0

        return sum(stack)


if __name__ == "__main__":
    solution = Solution()

    print(solution.calculate("3+2*2"))
    print(solution.calculate(" 3/2 "))
    print(solution.calculate(" 3+5 / 2 "))
    print(solution.calculate("14-3/2"))