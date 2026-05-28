class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])

                elif i == m - 1:
                    dungeon[i][j] = max(1, dungeon[i][j + 1] - dungeon[i][j])

                elif j == n - 1:
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])

                else:
                    need = min(dungeon[i + 1][j], dungeon[i][j + 1])
                    dungeon[i][j] = max(1, need - dungeon[i][j])

        return dungeon[0][0]


sol = Solution()

print(sol.calculateMinimumHP([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5]
]))

print(sol.calculateMinimumHP([[0]]))
print(sol.calculateMinimumHP([[100]]))
print(sol.calculateMinimumHP([[-3, 5]]))