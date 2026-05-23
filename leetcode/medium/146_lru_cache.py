class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node):
        prev_last = self.tail.prev

        prev_last.next = node
        node.prev = prev_last

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]

            node.val = value

            self.remove(node)
            self.add(node)

            return

        node = Node(key, value)

        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next

            self.remove(lru)

            del self.cache[lru.key]


if __name__ == "__main__":
    lru = LRUCache(2)

    lru.put(1, 1)
    lru.put(2, 2)

    print(lru.get(1))

    lru.put(3, 3)

    print(lru.get(2))

    lru.put(4, 4)

    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))