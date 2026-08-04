class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        d={i:[] for i in range(n)}

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        print(d)
        
        seen=set()
        def dfs(node):
            seen.add(node)
            for nei in d[node]:
                if nei not in seen:
                    dfs(nei)
        res=0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res