class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        cur = []
        def dfs(i, sum):
            if i > len(nums) - 1 or sum > target:
                return
            if sum == target:
                self.res.append(cur.copy())
                return
            
            cur.append(nums[i])
            sum += nums[i]
            dfs(i, sum)

            cur.pop()
            sum -= nums[i]
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return self.res



        