class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def back(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in dp:
                return dp[i]
            res = back(i+1)
            if i < len(s) -1:
                if s[i] == "1" or (s[i] == "2" and s[i+1] < "7"):
                    res += back(i+2)
            dp[i] = res
            return dp[i]
        return back(0)
