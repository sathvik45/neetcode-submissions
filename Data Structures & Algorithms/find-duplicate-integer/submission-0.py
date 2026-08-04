class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        check=[0]*(len(nums)+1)
        for i in nums:
            if check[i]>0:
                return i
            check[i]+=1
