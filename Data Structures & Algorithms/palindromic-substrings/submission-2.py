class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def pal(s):
            return s[::] == s[::-1]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if pal(s[i:j+1]):
                    res+=1
        return res
                