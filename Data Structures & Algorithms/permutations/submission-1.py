# we can select one out of 3, then we have to select from either one then next.
#we can iterate threough the list beacause all must be seleted atleast once
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        picked = [False for _ in nums]
        def dfs(cur):
            if len(cur) >= len(nums):
                res.append(cur.copy())
                return
            for j in range(len(nums)):
                if not picked[j]:
                    cur.append(nums[j])
                    picked[j] = True
                    dfs(cur)

                    cur.pop()
                    picked[j] = False
        dfs([])
        return res

                
        