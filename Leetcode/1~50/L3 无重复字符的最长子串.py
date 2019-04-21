class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        visit = [s[0]]
        result = [0 for i in range(len(s))]
        result[0] = 1
        for i in range(1, len(s)):
            if s[i] not in visit:
                visit += [s[i]]
                result[i] = result[i - 1] + 1
            else:
                visit.append(s[i])
                x = visit.pop(0)
                while x != s[i]:
                    x = visit.pop(0)
                result[i] = len(visit)
        return max(result)
