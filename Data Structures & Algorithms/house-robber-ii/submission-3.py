class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[-1]*len(nums)
        def dfs(i,flag):
            if (i>=len(nums)) or (flag==True and i==len(nums)-1):
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            dp[i]=max(dfs(i+1,flag),nums[i]+dfs(i+2,flag))
            return dp[i]
        zero=dfs(0,True)
        dp=[-1]*len(nums)
        first=dfs(1,False)
        return max(zero,first)
        
    