class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        l,r = 0,0

        for r in range(len(s)):
            if d.get(s[r],0) == 0:
                d[s[r]] = 1
            else:
                while s[l] != s[r]:
                    d[s[l]] = 0
                    l+=1
                l+=1
            res = max(res,r-l+1)
        return res