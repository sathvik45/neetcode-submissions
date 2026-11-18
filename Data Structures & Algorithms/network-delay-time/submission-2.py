class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((t,v))
        
        minheap = [(0,k)]
        seen = set()
        time = 0
        while minheap:
            t, node = heapq.heappop(minheap)
            if node in seen:
                continue
            seen.add(node)
            for t2,node2 in adj[node]:
                if node2 not in seen:
                    heapq.heappush(minheap,(t+t2,node2))
            time = t
            
        return time if len(seen) == n else -1

