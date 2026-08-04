class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i,j = 0, 0
        res = float('-inf')

        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s += nums[j]
                res = max(res, s)
        return res
        