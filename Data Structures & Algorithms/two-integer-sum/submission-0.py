class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j=0,1
        while 1:
            if target -nums[j] == nums[i]:
                return [i,j]
            j+=1
            if j>=len(nums):
                i+=1
                j=i+1
