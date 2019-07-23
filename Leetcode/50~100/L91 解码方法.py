'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6)
'''


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        result = [1 for i in range(len(s) + 1)]
        j = 0
        for i in range(1, len(s)):
            j = i + 1
            if s[i] != '0':
                if s[i - 1] == 0:
                    result[j] = result[j - 1]
                else:
                    if 10 < int(s[i - 1:i + 1]) < 27:
                        result[j] = result[j - 1] + result[j - 2]
                    else:
                        result[j] = result[j - 1]
            else:
                if s[i - 1] == '1' or s[i - 1] == '2':
                    result[j] = result[j - 2]
                else:
                    return 0
        return result[j]

