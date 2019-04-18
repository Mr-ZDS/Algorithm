'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

def Matrix():
    n = int(input("请输入螺旋矩阵的行数:"))
    matrix = [[0 for i in range(n)] for j in range(n)]
    row, col = n - 1, n - 1
    start = 0
    number = 1

    def Print_M(row, col, start, number):
        if row == 0:
            if n % 2 == 1:
                matrix[n // 2][n // 2] = n * n

        else:
            for i in range(start, col):  # 打印上横行
                matrix[start][i] = number
                number += 1
            for i in range(start, row):  # 打印右竖行
                matrix[i][col] = number
                number += 1
            for i in range(col, start, -1):
                matrix[row][i] = number
                number += 1
            for i in range(row, start, -1):
                matrix[i][start] = number
                number += 1
            return Print_M(row - 1, col - 1, start + 1, number)

    Print_M(row, col, start, number)
    for i in range(n):
        for j in range(n):
            print(format(matrix[i][j], '3'), end = ' ')
        print()
Matrix()

'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        row, col = n - 1, n - 1
        start = 0
        number = 1

        def Print_M(row, col, start, number):
            if row == 0:
                if n % 2 == 1:
                    matrix[n // 2][n // 2] = n * n

            else:
                for i in range(start, col):  # 打印上横行
                    matrix[start][i] = number
                    number += 1
                for i in range(start, row):  # 打印右竖行
                    matrix[i][col] = number
                    number += 1
                for i in range(col, start, -1):
                    matrix[row][i] = number
                    number += 1
                for i in range(row, start, -1):
                    matrix[i][start] = number
                    number += 1
                return Print_M(row - 1, col - 1, start + 1, number)
        Print_M(row, col, start, number)
        return matrix
'''
