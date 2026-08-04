class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={']':'[','}':'{',')':'('}
        for i in s:
            if i in d.keys():
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if stack:
            return False
        return True
        