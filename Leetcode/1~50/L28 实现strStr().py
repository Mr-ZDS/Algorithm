class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        length = len(needle)
        if length == 0:
            return 0

        for i in range(len(haystack)):
            if haystack[i] != needle[0]:
                continue;
            elif haystack[i:i + length] == needle:
                return i
        return -1
