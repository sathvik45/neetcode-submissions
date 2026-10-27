class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj ={i:[] for i in range(numCourses)}
        for u,v in prerequisites:
            adj[u].append(v)
        print(adj)
        seen = set()
        visit = set()
        cur = []
        def dfs(i):
            if i in seen:
                return False
            if i in visit:
                return True
            seen.add(i)
            
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            seen.remove(i)
            cur.append(i)
            visit.add(i)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return cur

            
        