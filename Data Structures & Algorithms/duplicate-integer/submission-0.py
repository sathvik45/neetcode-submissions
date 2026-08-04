class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=0
            elif d[i]==0:
                return True
        return False
        