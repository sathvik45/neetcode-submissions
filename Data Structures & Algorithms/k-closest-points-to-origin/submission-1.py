class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap =[]
        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(minheap,(distance,point))

        res =[]
        while k:
            key = heapq.heappop(minheap)
            print(type(key))
            res.append(key[1])
            k-=1
        return res


        