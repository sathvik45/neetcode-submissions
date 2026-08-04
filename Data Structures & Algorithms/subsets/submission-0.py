class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        for num in nums:
            new_subsets=[]
            for subset in res:
                new_subset= subset + [num]
                new_subsets.append(new_subset)
            res.extend(new_subsets)
        return res
            