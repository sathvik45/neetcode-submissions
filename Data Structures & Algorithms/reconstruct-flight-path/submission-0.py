class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        res = ['JFK']

        def dfs(scr):
            if len(res) == len(tickets) + 1:
                return True
            if scr not in adj:
                return False
            
            temp = list(adj[scr])
            for i, v in enumerate(temp):
                adj[scr].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[scr].insert(i,v)
                res.pop()
            return False
        dfs('JFK')
        return res

