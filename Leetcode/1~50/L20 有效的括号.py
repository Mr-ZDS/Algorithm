class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                lis.append(i)
            else:
                if len(lis) != 0:
                    visit = lis.pop()
                    if (visit == '(' and i != ')') or (visit == '[' and i != ']') or (visit == '{' and i != '}'):
                        return False
                else:
                    return False
        if len(lis) == 0:
            return True
        else:
            return False
