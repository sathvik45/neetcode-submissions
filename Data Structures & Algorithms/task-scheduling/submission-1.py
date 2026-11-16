class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for x in tasks:
            freq[x] = freq.get(x,0) +1
        print(freq)
        maxheap = [-x for x in freq.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()#(frq,time)
        while maxheap or q:
            time+=1
            if maxheap:
                f = heapq.heappop(maxheap)
                f+=1
                if f:
                    q.append((f,time+n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
            
        return time

            
            

        