from typing import List


class Iterator:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.index = 0

    def hasNext(self) -> bool:
        return self.index < len(self.nums)

    def next(self) -> int:
        value = self.nums[self.index]
        self.index += 1
        return value


class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.has_peeked = False
        self.peeked_element = None

    def peek(self):
        if not self.has_peeked:
            self.peeked_element = self.iterator.next()
            self.has_peeked = True
        return self.peeked_element

    def next(self):
        if not self.has_peeked:
            return self.iterator.next()

        result = self.peeked_element
        self.has_peeked = False
        self.peeked_element = None
        return result

    def hasNext(self):
        return self.has_peeked or self.iterator.hasNext()


if __name__ == "__main__":
    nums = [1, 2, 3]

    iterator = PeekingIterator(Iterator(nums))

    print("peek():", iterator.peek())      # 1
    print("next():", iterator.next())      # 1
    print("next():", iterator.next())      # 2
    print("peek():", iterator.peek())      # 3
    print("hasNext():", iterator.hasNext())  # True
    print("next():", iterator.next())      # 3
    print("hasNext():", iterator.hasNext())  # False