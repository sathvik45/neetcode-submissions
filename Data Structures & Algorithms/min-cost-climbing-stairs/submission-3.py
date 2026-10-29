class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        def dfs(i,cur):
            if i >= n:
                return cur
            if (i,cur) in dp:
                return dp[(i,cur)]
            cur += cost[i]
            dp[(i,cur)] = min(dfs(i+1,cur),dfs(i+2,cur))
            return dp[(i,cur)]
        
        return min(dfs(0,0),dfs(1,0))
