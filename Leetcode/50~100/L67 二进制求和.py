'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''

def addBinary(a, b) :
    n = max(len(a), len(b)) + 1
    a, b = a.zfill(n), b.zfill(n)
    visit , res = 0, ''
    for i in range(n-1, -1, -1):
        t = int(a[i]) + int(b[i]) + visit
        if t >= 2:
            visit = 1
            res += str(t - 2)
        else:
            res += str(t)
            visit = 0
    if res[-1] == '0':
        return res[:-1][::-1]
    return res[::-1]

a = "1111110"
b = "0"
print(addBinary(a, b))