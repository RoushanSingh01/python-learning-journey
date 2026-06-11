from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def dfs(node: int, parent: int = 0) -> int:
            max_depth = 0

            for neighbor in graph[node]:
                if neighbor != parent:
                    max_depth = max(
                        max_depth,
                        dfs(neighbor, node) + 1
                    )

            return max_depth

        n = len(edges) + 1

        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        depth = dfs(1)

        return pow(2, depth - 1, 1_000_000_007)


if __name__ == "__main__":
    solution = Solution()

    print(solution.assignEdgeWeights([[1, 2]]))
    print(solution.assignEdgeWeights([[1, 2], [1, 3]]))
    print(solution.assignEdgeWeights([[1, 2], [2, 3], [3, 4]]))