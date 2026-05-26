class MinStack:

    def __init__(self):
        self.data = []

    def push(self, value):
        if not self.data or value < self.data[-1][1]:
            self.data.append([value, value])
        else:
            self.data.append([value, self.data[-1][1]])

    def pop(self):
        self.data.pop()

    def top(self):
        return self.data[-1][0]

    def getMin(self):
        return self.data[-1][1]


if __name__ == "__main__":
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    print(stack.getMin())  # -3

    stack.pop()

    print(stack.top())     # 0
    print(stack.getMin())  # -2