class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        candidates.sort()
        curr=[]
        def dfs(i,s):
            if s == target:
                print(curr)
                res.add(tuple(curr.copy()))
                return
            if i >= len(candidates) or s > target:
                print(curr)
                return

            curr.append(candidates[i])
            s+=candidates[i]
            dfs(i+1,s)

            temp=curr.pop()
            s-=temp
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,s)
        dfs(0,0)
        ret=[]
        for i in res:
            ret.append(list(i))
        return ret
