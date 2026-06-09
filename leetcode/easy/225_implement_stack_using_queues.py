from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


if __name__ == "__main__":
    stack = MyStack()

    stack.push(1)
    stack.push(2)

    print(stack.top())
    print(stack.pop())
    print(stack.empty())

    stack.push(3)

    print(stack.top())
    print(stack.pop())
    print(stack.empty())