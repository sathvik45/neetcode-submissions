class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=[]
        for i,j in points:
            distance.append(((i**2+j**2)**0.5,[i,j]))

        print(distance)
        heapq.heapify(distance)
        res=[]
        while k:
            res.append(heapq.heappop(distance)[1])
            k-=1
        return res

        