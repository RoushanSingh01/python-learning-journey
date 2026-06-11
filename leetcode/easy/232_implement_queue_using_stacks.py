class MyQueue:
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack

    def _move(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(
                    self.input_stack.pop()
                )


if __name__ == "__main__":
    queue = MyQueue()

    queue.push(1)
    queue.push(2)

    print(queue.peek())
    print(queue.pop())
    print(queue.empty())

    queue.push(3)

    print(queue.peek())
    print(queue.pop())
    print(queue.pop())
    print(queue.empty())