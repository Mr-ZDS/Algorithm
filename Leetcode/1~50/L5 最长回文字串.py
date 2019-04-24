'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"
'''


class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return s
        if len(set(s)) == 1:
            return s

        n = len(s)
        left = 0
        right = 0
        max = 0
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if s[i] == s[j]:
                    if (i - j == 1) or dp[j + 1][i - 1] == 1:
                        dp[j][i] = 1

                if dp[j][i] == 1 and max < i - j + 1:
                    max = i - j + 1
                    left = j
                    right = i
            dp[i][i] = 1
        return s[left: right + 1]
