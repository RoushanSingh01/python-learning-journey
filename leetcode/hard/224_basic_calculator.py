class Solution:
    def calculate(self, s):
        result = 0
        number = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == "+":
                result += sign * number
                number = 0
                sign = 1

            elif ch == "-":
                result += sign * number
                number = 0
                sign = -1

            elif ch == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif ch == ")":
                result += sign * number
                number = 0

                result *= stack.pop()
                result += stack.pop()

        return result + sign * number


if __name__ == "__main__":
    solution = Solution()

    print(solution.calculate("1 + 1"))
    print(solution.calculate(" 2-1 + 2 "))
    print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))
    print(solution.calculate("1-(-2)"))
    print(solution.calculate("2-(5-6)"))