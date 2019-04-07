# 动态规划
visit = int(input('请输入背包重量:'))

value = [0, 1500, 3000, 2000, 2000]  # 对应物品的价值
weight = [0, 1, 4, 3, 1]  # 对应物品的重量

index = []  # 记录装入背包的物品索引
list = [[0 for col in range(visit + 1)] for row in range(len(weight))]


def DP(visit, weight, value, list, index):
    for i in range(1, len(weight)):
        for j in range(1, visit + 1):
            if j >= weight[i]:
                list[i][j] = max(list[i - 1][j], value[i] + list[i - 1][j - weight[i]])
            else:
                list[i][j] = list[i - 1][j]

    #寻找最大值中放入的物品的的索引
    for i in range(len(weight) - 1, 0, -1):
        if list[i][j] > list[i - 1][j]:
            index.append(i)
            j = j - weight[i]

    print(list[len(weight) - 1][visit])
    print(index[::-1])
    # 输出二维数组列表
    for row in range(1, len(weight)):
        for col in range(1, visit + 1):
            print(list[row][col], end = '  ')
        print()


DP(visit, weight, value, list, index)
