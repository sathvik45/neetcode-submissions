class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i,cur):
            if (i,cur) in dp:
                return dp[(i,cur)]
            if i == len(nums):
                if cur == target:
                    return 1
                return 0
            dp[(i,cur)] = dfs(i+1,cur+nums[i])+dfs(i+1,cur-nums[i])
            return dp[(i,cur)]
        
        return dfs(0,0)