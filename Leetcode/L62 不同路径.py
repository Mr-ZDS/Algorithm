def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    lis = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                if obstacleGrid[i][j] == 0:
                    lis[i][j] = 1
            else:
                if obstacleGrid[i][j] == 0:
                    lis[i][j] = lis[i - 1][j] + lis[i][j - 1]
    return lis[m - 1][n - 1]


lis = [[0 for i in range(3)] for j in range(3)]
lis[1][1] = 1
print(lis)
print(uniquePathsWithObstacles(lis))
