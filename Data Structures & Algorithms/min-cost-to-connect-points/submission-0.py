class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)

        for src in points:
            for des in points:
                if src == des:
                    continue
                adj[(src[0],src[1])].append((abs(src[0]-des[0])+abs(src[1]-des[1]),(des[0],des[1])))
        seen = set()
        minheap = [(0,tuple(points[0]))]
        res = 0
        while len(seen) < len(points):
            cost, node = heapq.heappop(minheap)
            if node in seen:
                continue
            seen.add(node)
            res+=cost
            for nei_cost, nei in adj[node]:
                if nei not in seen:
                    heapq.heappush(minheap,(nei_cost,nei))
        
        return res

            