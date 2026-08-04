class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        curr=[]
        def dfs(i,s):
            if s == target:
                res.add(tuple(curr.copy()))
                return
            if i >= len(candidates):
                return

            curr.append(candidates[i])
            s+=candidates[i]
            dfs(i+1,s)

            temp=curr.pop()
            s-=temp
            dfs(i+1,s)
        dfs(0,0)
        ret=[]
        for i in res:
            ret.append(list(i))
        return ret
