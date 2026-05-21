from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        visited = {}

        def dfs(current):
            if current in visited:
                return visited[current]

            clone = Node(current.val)
            visited[current] = clone

            clone.neighbors = [dfs(neighbor) for neighbor in current.neighbors]

            return clone

        return dfs(node)


def print_graph(node):
    visited = set()
    queue = deque([node])

    while queue:
        current = queue.popleft()

        if current.val in visited:
            continue

        visited.add(current.val)

        neighbors = [neighbor.val for neighbor in current.neighbors]
        print(f"Node {current.val}: {neighbors}")

        for neighbor in current.neighbors:
            queue.append(neighbor)


def run_tests():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    solution = Solution()
    cloned = solution.cloneGraph(node1)

    print("Original Graph:")
    print_graph(node1)

    print("\nCloned Graph:")
    print_graph(cloned)


if __name__ == "__main__":
    run_tests()