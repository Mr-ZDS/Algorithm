class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        while n:
            result += n // 5
            n = n // 5
        return result