class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i : [] for i in range(numCourses)}
        for c, p  in prerequisites:
            premap[c].append(p)
        
        visit = set()
        seen = set()
        res = []
        def dfs(i):
            if i in visit:
                return False
            if i in seen:
                return True
            visit.add(i)
            for nei in premap[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            seen.add(i)
            res.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
