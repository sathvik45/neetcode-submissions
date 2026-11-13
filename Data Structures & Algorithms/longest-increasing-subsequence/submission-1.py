class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     tres = 0
        #     for j in range(i,len(nums)):
        #         if nums[j] > temp:
        #             tres +=1
        #             temp = nums[j]
        #     res = max(res,tres)
        # return res
        dp = {}
        def dfs(i,prev):
            if i == len(nums):
                return 0
            if (i,prev) in dp:
                return dp[(i,prev)]
            res = dfs(i+1,prev)
            if prev==-1 or nums[i] > nums[prev]:
                res = max(res,1 + dfs(i+1,i))
            dp[(i,prev)] = res
            return res
        return dfs(0,-1)