class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)

        def dfs(i, par):
            seen.add(i)
            for nei in d[i]:
                if nei == par:
                    continue
                if nei in seen:
                    return False
                if not dfs(nei, i):
                    return False
            return True
        
        for e, v in edges:
            d[e].append(v)
            d[v].append(e)
            seen = set()
            if not dfs(e, -1):
                return [e, v]
                