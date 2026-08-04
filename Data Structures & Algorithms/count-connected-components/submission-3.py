class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d={i:[] for i in range(n)}

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        res = 0
        seen = set()

        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for nei in d[i]:
                dfs(nei)

        for i in range(n):
            if i not in seen:
                res+=1
                dfs(i)
        return res