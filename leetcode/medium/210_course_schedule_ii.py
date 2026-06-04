from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []

        while q:
            node = q.popleft()
            order.append(node)

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        return order if len(order) == numCourses else []

if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    print(Solution().findOrder(numCourses, prerequisites))