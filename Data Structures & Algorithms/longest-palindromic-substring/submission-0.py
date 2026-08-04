class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_length=0
        res=""

        for i in range(len(s)):
            for j in range(i,len(s)):
                left,right=i,j
                while left<right and s[left] == s[right]:
                    left+=1
                    right-=1
                
                if left>=right and j-i+1>res_length:
                    res=s[i:j+1]
                    res_length=j-i+1
        return res
        