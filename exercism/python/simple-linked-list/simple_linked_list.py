"""Simple linked list implementation."""


class Node:
    """Node in a linked list."""

    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, node):
        self._next = node


class LinkedList:
    """Singly linked list."""

    def __init__(self, values=None):
        self._head = None

        if values is not None:
            for value in values:
                self.push(value)

    def __len__(self):
        count = 0
        current_node = self._head

        while current_node is not None:
            count += 1
            current_node = current_node.next()

        return count

    def head(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        new_node = Node(value)
        new_node.set_next(self._head)
        self._head = new_node

    def pop(self):
        current_node = self.head()
        value = current_node.value()
        self._head = current_node.next()
        return value

    def __iter__(self):
        current_node = self._head

        while current_node is not None:
            yield current_node.value()
            current_node = current_node.next()

    def reversed(self):
        return LinkedList(list(self))


class EmptyListException(Exception):
    """Raised when operating on an empty list."""

    def __init__(self, message):
        super().__init__(message)