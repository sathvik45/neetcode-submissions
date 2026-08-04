class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]

        def ispal(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i,j=i+1,j-1
            return True
    
        def back(i):
            if i>=len(s):
                res.append(curr.copy())
                return
            
            for j in range(i,len(s)):
                if ispal(s,i,j):
                    curr.append(s[i:j+1])
                    back(j+1)
                    curr.pop()
        back(0)
        return res
