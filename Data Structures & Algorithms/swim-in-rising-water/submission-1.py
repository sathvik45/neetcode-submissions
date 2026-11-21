class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        seen = set()
        minheap = [(grid[0][0],(0,0))]
        res = 0
        while minheap:
            time,node = heapq.heappop(minheap)
            if node in seen:
                continue
            seen.add(node)
            res = max(res,time)
            if node == (n-1,m-1):
                break
            print(node)
            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                r,c = node[0]+di,node[1]+dj
                if 0<=r<n and 0<=c<m and (r,c) not in seen:
                    heapq.heappush(minheap,(grid[r][c],(r,c)))
        return res