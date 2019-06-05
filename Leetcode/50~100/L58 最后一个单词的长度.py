# 解法一
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        return len(s.split()[-1])


# 解法二
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        visit = ''
        for i in s:
            if i != ' ':
                visit += i
            else:
                visit = ''
        return len(visit)
