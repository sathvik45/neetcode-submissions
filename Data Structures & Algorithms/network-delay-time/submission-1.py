class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for i, g in enumerate(times):
            # print(i, g)
            u, v, t = g
            adj[u].append((t, v)) 
        print(adj) 

        minheap = [(0, k)]
        seen = set()
        t = 0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in seen:
                continue
            seen.add(n1)
            t = w1
            for w2, n2 in adj[n1]:
                if n2 not in seen:
                    heapq.heappush(minheap,(w1 + w2, n2))
            
        return t if len(seen) == n else -1

