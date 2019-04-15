class Solution:
    def reverse(self, x: int) -> int:
        lis = list(str(x))
        while lis[-1] == 0:
            lis.pop()

        if lis[0] == '-':
            visit = lis.pop(0)
            lis.reverse()
            lis.insert(0, visit)
            res = ''.join(lis)
            result = int(res)
            if result < (-2) ** 31:
                return 0
            else:
                return result
        else:
            lis.reverse()
            res = ''.join(lis)
            result = int(res)
            if result > (2 ** 31 - 1):
                return 0
            else:
                return result
