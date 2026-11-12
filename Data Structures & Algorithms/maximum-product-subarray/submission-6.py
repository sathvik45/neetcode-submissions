class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        max_nums,min_nums = 1,1

        for n in nums:
            temp = max_nums
            max_nums = max(n*max_nums,n*min_nums,n)
            min_nums = min(temp*n,n*min_nums,n)
            res = max(res,max_nums)
        
        return res
        
