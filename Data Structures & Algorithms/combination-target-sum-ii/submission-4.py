class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = set()
        cur = []
        def dfs(i, sum):
            if sum == target:
                self.res.add(tuple(cur.copy()))
                return 

            if  i > len(candidates)-1 or sum > target:
                return
            
            
            cur.append(candidates[i])
            sum += candidates[i]
            dfs(i+1, sum)

            temp = cur.pop()
            sum -= temp
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, sum)

        dfs(0,0)
        ret = []
        for i in self.res:
            ret.append(list(i))
        return ret
