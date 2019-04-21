'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def Eec(s):
            for i in range(len(s)):
                if s[i].count('(') == n:
                    s[i] += ')'
                elif s[i].count('(') > s[i].count(')'):
                    s.append(s[i] + '(')
                    s[i] += ')'
                else:
                    s[i] += '('
            if len(s[0]) == 2 * n:
                return
            Eec(s)

        s = ['(']
        Eec(s)
        return s
