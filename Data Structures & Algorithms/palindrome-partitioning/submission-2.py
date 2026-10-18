class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def pal(cur):
            return cur == cur[::-1]
        def back(i,cur):
            if i == len(s):
                res.append(cur.copy())
                return
            
            for j in range(i,len(s)):
                if pal(s[i:j+1]):
                    cur.append(s[i:j+1])    
                    back(j+1,cur)

                    cur.pop()
        back(0,[])
        return res

