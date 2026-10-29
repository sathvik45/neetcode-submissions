class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(step):
            if step > n:
                return 0
            if step == n:
                return 1
            if step in dp:
                return dp[step]
            dp[step] = dfs(step + 1) + dfs(step + 2)
            return dp[step]
        
        return dfs(0)
        