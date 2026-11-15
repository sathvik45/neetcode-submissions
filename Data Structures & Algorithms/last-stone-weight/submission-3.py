class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        
        while len(maxheap)>1:
            x, y = heapq.heappop(maxheap),heapq.heappop(maxheap)
            heapq.heappush(maxheap,(-abs(x-y)))
        if len(maxheap):
            return -maxheap[0]
        return 0


        