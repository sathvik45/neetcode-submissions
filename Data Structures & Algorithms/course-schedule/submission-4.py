# a dp optimisation can be done
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i : [] for i in range(numCourses)}
        for c, e in prerequisites:
            graph[c].append(e)
        print(graph)

        visit = set()

        def dfs(i):
            visit.add(i)
            for nei in graph[i]:
                if nei in visit:
                    return False
                if not dfs(nei):
                    return False
            visit.remove(i)
            return True
        for v, e in graph.items():

            if not dfs(v):
                return False
        return True