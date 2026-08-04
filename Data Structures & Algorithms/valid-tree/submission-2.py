class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        print(d)
        seen=set()
        def dfs(i,parent):
            
            print(i)
            seen.add(i)
            for nei in d[i]:
                if nei == parent:
                    continue
                if nei in seen:
                    return False
                if not dfs(nei,i):
                    return False
            return True
        
        return dfs(0,-1) and n==len(seen)
