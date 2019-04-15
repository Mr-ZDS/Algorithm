import numpy as np
matrix=np.random.randint(0,9,size=[3,4])     #生成随机测试二维数组
print(matrix)

row=len(matrix)
col=len(matrix[0])
lis_r=[]
lis_c=[]

for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            lis_r.append(i)
            lis_c.append(j)
for i in lis_r:
    matrix[i]=0
for i in lis_c:
    for j in range(row):
        matrix[j][i]=0

print(matrix)
