class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)

        def dfs(course):
            if state[course] == 1:
                return True
            if state[course] == -1:
                return False

            state[course] = -1

            for nxt in graph[course]:
                if not dfs(nxt):
                    return False

            state[course] = 1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]

    print(Solution().canFinish(numCourses, prerequisites))