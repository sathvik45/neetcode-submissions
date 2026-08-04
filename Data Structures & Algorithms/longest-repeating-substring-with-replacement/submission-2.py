class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res=0
        for i in range(len(s)):
            charset=defaultdict(int)
            for j in range(i,len(s)):
                charset[s[j]]+=1
                if charset and j-i- max(charset.values()) <= k-1:
                    res=max(res,j-i+1)
            
        return res


        