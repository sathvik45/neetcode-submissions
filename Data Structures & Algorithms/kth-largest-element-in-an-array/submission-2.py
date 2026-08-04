class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-x for x in nums]
        heapq.heapify(maxheap)
        res = None
        while k:
            res = heapq.heappop(maxheap)
            k -= 1
        return -res