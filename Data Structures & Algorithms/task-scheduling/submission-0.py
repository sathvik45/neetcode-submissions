class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = defaultdict(int)
        for t in  tasks:
            d[t] = d.get(t,0) + 1
        print(d)
        maxheap = [-x for x in d.values()]
        print(maxheap)
        heapq.heapify(maxheap)
        time = 0
        q= deque()
        while maxheap or q:
            time += 1
            if maxheap:
                c = heapq.heappop(maxheap)
                c += 1
                if c:
                  q.append((c,time + n))
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        return time
