class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x,y in points:        
            heapq.heappush(minheap,[(x**2+y**2)**0.5,x,y])

        res = []
        while k:
            res.append(heapq.heappop(minheap)[1:])
            k-=1
        return res