class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = {}
        def dfs(i,cur):
            if i >= len(nums):
                return cur == 0
            if cur < 0:
                return False
            if (i,cur) in dp:
                return dp[(i,cur)]
            dp[(i,cur)] = dfs(i+1,cur) or dfs(i+1,cur-nums[i])
            return dp[(i,cur)]
        
        return dfs(0,sum(nums)//2)
        