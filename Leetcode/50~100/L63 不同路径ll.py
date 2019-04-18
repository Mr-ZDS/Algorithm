class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        lis = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                lis[0][i] = 1
            else:
                break
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                lis[i][0] = 1
            else:
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    lis[i][j] = lis[i - 1][j] + lis[i][j - 1]
        return lis[m - 1][n - 1]
