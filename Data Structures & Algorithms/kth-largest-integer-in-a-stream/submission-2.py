class KthLargest:
    minheap=[]
    ki=0
    def __init__(self, k: int, nums: List[int]):
        self.ki=k
        self.minheap=nums
        heapq.heapify(self.minheap)
        while len(self.minheap)>k:
            heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap)>self.ki:
            heapq.heappop(self.minheap)
        return self.minheap[0]

            
        
