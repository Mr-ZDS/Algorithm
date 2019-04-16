#二维数组踩坑

#二维数组初始化
n=int(input())
list=[[0 for i in range(n)] for j in range(n)]      #前为列数，后为行数
print(list) 
list[0][1]=1
print(list)


#用*初始化二维数组在修改时会出现错误
n=int(input())
list1=[[0]*n]*n
print(list1)
list1[0][1]=1
print(list1)


list2 = list(set([tuple(t) for t in li]))  # 二维list去重