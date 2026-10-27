class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i : [] for i in range(1,n+1)}
        seen = set()
        def dfs(i,par):
            if i in seen:
                return False
            seen.add(i)
            for nei in adj[i]:
                if nei == par:
                    continue
                if not dfs(nei,i):
                    return False
            seen.remove(i)
            return True
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            print(u,v)
            print(dfs(u,-1))
            if not dfs(u,-1):
                return [u,v]
        return []

            