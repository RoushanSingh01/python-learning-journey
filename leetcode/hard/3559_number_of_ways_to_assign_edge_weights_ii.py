from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1_000_000_007
        n = len(edges) + 1
        LOG = n.bit_length()

        graph = [[] for _ in range(n + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]

        stack = [(1, 0)]
        while stack:
            node, parent = stack.pop()
            up[0][node] = parent

            for nxt in graph[node]:
                if nxt != parent:
                    depth[nxt] = depth[node] + 1
                    stack.append((nxt, node))

        for k in range(1, LOG):
            prev = up[k - 1]
            curr = up[k]
            for node in range(1, n + 1):
                curr[node] = prev[prev[node]]

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            bit = 0

            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]

            return up[0][a]

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        answer = []

        for u, v in queries:
            ancestor = lca(u, v)
            distance = depth[u] + depth[v] - 2 * depth[ancestor]

            if distance == 0:
                answer.append(0)
            else:
                answer.append(pow2[distance - 1])

        return answer


if __name__ == "__main__":
    solution = Solution()

    edges1 = [[1, 2]]
    queries1 = [[1, 2], [1, 1]]
    print("Test 1:", solution.assignEdgeWeights(edges1, queries1))
    print("Expected:", [1, 0])

    edges2 = [[1, 2], [1, 3], [3, 4]]
    queries2 = [[2, 3], [2, 4], [3, 4]]
    print("\nTest 2:", solution.assignEdgeWeights(edges2, queries2))
    print("Expected:", [1, 2, 1])

    edges3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    queries3 = [[1, 5], [2, 5], [3, 5], [4, 5]]
    print("\nTest 3:", solution.assignEdgeWeights(edges3, queries3))
    print("Expected:", [8, 4, 2, 1])

    edges4 = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7]]
    queries4 = [[4, 5], [4, 6], [5, 7], [6, 7]]
    print("\nTest 4:", solution.assignEdgeWeights(edges4, queries4))