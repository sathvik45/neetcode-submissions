class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stoneN=[-s for s in stones]
        heapq.heapify(stoneN)
        while len(stoneN)>1:
            x,y=heapq.heappop(stoneN),heapq.heappop(stoneN)
            if x==y:
                continue
            heapq.heappush(stoneN,-((abs(x)-abs(y))))
        if len(stoneN):
            return -stoneN[0]
        return 0