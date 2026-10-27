class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0
        adj = {i:[] for i in range(n)}

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        cycle = set()
        seen = set()
        
        def dfs(i):
            seen.add(i)
            for nei in adj[i]:
                if nei not in seen:
                    dfs(nei)
        
        for i in range(n):
            if i not in seen:
                dfs(i)
                res += 1
        return res