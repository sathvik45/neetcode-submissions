class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        seen=[]
        for r in range(len(s)):
            if s[r] not in seen:
                seen.append(s[r])
            else:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.append(s[r])
            res=max(res,r-l+1)
        return res