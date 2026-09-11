class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i in range(len(nums)):
            if dp.get(nums[i],-1) == -1:
                dp[target - nums[i]] = i
            else:
                return [dp[nums[i]],i]