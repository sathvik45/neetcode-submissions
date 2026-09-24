class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        cur = []
        def back(i):
            if i >= len(nums) or sum(cur) > target:
                return
            if sum(cur) == target:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            back(i)
            cur.remove(nums[i])
            back(i+1)
        back(0)
        return res