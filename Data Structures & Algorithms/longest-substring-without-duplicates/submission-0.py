class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        
        res=0
        while i<len(s):
            j=i
            seen=[]
            c=0
            while j<len(s):
                if s[j] not in seen:
                    seen.append(s[j])
                    c+=1
                    j+=1
                else:
                    break
            
            res=max(res,c)
            i+=1
        return res