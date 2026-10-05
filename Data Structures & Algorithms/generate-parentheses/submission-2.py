class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back(cur,openN,closeN):
            if openN==closeN==n:
                res.append("".join(cur))
                return
            if openN<n:
                cur.append('(')
                back(cur,openN+1,closeN)
                cur.pop()
            if closeN<openN:
                cur.append(')')
                back(cur,openN,closeN+1)
                cur.pop()
        back([],0,0)
        return res
            
        