class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for u,v in prerequisites:
            adj[v].append(u)
        print(adj)

        def dfs(i):
            if i in seen:
                return False
            if adj[i] == []:
                return True
            seen.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            seen.remove(i)
            adj[i] = []

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        