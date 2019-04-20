# 递归解决迷宫问题
import numpy as np

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向


def Maze(maze, pos, end):
    maze[pos[0]][pos[1]] = 2
    if pos == end:
        print(pos)
        return True
    for i in range(4):
        next = pos[0] + dir[i][0], pos[1] + dir[i][1]
        if maze[next[0]][next[1]] == 0:
            if Maze(maze, next, end):
                print(pos)
                return True
    return False


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], ]

print('迷宫大小:', np.shape(maze))  # 获得迷宫大小
print("迷宫：", Maze(maze, pos = (1, 1), end = (10, 12)))
for i in range(12):
    print(maze[i])
