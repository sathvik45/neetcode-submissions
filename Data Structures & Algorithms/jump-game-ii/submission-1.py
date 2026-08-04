class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}
        def backtrack(i):
            if i in dp:
                return dp[i]
            if i >= len(nums)- 1:
                return 0
            res = float('inf')
            for j in range(1,nums[i]+1):
                res = min(res,1 + backtrack(i + j))
            dp[i] = res
            return dp[i]
        return backtrack(0)

        