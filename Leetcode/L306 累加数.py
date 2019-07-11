def isAdditiveNumber(num):
    res = []  # 将每次符合条件的数压入栈中

    def dfs(num, count):  # count 记录当前找到的数的个数
        # print(count,num,res)
        if count >= 3 and len(num) == 0:  # 当数量不少于三个且字符串为空，返回True
            return True
        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == "0":  # 去掉0开头的数，但一位数的时候可以是0， 如1.0.1
                continue

            if count < 2:  # 栈中数量不足三个，直接压入栈中
                res.append(int(num[:i]))
                if dfs(num[i:], count + 1):  # 继续判断剩余字符串
                    return True
                res.pop(-1)  # 每次回溯完成后要恢复原栈

            else:  # 当个数足够两个，那么就开始判断前两个数之和是否与当前数相等
                if res[-1] + res[-2] == int(num[:i]):
                    res.append(int(num[:i]))
                    if dfs(num[i:], count + 1):
                        return True
                    res.pop(-1)
        return False

    return dfs(num, 0)

print(isAdditiveNumber('112358'))