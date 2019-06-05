'''
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''

def dd(n):
    count=0
    for i in range(2,n):
        for j in range(2,i):
            if i%j==0:
                break
        count+=1
    return count

print(dd(10))

