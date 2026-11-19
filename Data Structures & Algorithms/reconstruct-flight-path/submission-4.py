class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)

        adj = defaultdict(list)
        for src,des in tickets:
            adj[src].append(des)

        res = []
        def dfs(src):
            while adj[src]:
                dfs(adj[src].pop())
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
