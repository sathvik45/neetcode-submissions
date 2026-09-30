class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def back(i,cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if sum(cur) > target or i >= len(nums):
                return
            
            cur.append(nums[i])
            back(i,cur)
            cur.remove(nums[i])
            back(i + 1,cur)
        back(0,[])
        return res

