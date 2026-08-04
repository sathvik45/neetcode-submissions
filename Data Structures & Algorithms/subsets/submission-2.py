#we can divide the decision either by taking a num into account or not
#we could get an empty and take one, if we take one we can increament the index and make furthermore desciosns

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(i, cur):
            if i > len(nums)-1:
                self.res.append(cur.copy())
                return 
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.remove(nums[i])
            dfs(i + 1, cur)
        
        dfs(0, [])
        return self.res
        
