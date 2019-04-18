# 动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if row == 0 or col == 0:
            return 0
        visit = [[0 for i in range(col)] for j in range(row)]
        visit[0][0] = grid[0][0]
        for i in range(1, col):
            visit[0][i] = visit[0][i - 1] + grid[0][i]
        for i in range(1, row):
            visit[i][0] = visit[i - 1][0] + grid[i][0]
        if row == 1:
            return visit[0][col - 1]
        if col == 1:
            return visit[row - 1][0]
        for i in range(1, row):
            for j in range(1, col):
                visit[i][j] = min(visit[i - 1][j], visit[i][j - 1]) + grid[i][j]
        return visit[row - 1][col - 1]
