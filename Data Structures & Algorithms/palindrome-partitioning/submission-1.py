class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def ispal(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i+1, j-1
            return True
        def back(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return 
            for j in range(i,len(s)):
                print(s[i:j+1])
                if ispal(s, i, j):
                    cur.append(s[i:j + 1])
                    back(j + 1, cur)
                    cur.pop()
        back(0, [])
        print(res)
        return res