class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        
        
        print(d)
        seen=set()
        def dfs(node,parent):
            seen.add(node)
            for nei in d[node]:
                if nei==parent:
                    continue
                if nei in seen:
                    return False
                if not dfs(nei,node):
                    return False
            return True

        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
            seen=set()
            if not dfs(u,-1):
                return [u,v]
        return []