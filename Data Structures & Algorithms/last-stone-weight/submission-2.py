class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for x in stones:
            heapq.heappush(maxheap, -x)

        print(maxheap)
        while len(maxheap) > 1:
            x, y = heapq.heappop(maxheap), heapq.heappop(maxheap)
            if x - y != 0:
                heapq.heappush(maxheap, x-y)
        return -maxheap[0] if maxheap else 0
        