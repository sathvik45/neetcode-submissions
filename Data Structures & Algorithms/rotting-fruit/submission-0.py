class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        fresh,time=0,0
        directions=[[0, 1], [0, -1], [1, 0], [-1, 0]]
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))

        while fresh>0 and q:
            length=len(q)
            for ele in range(length):
                i,j=q.popleft()
                for di,dj in directions:
                    r,c=i+di,j+dj
                    if (r in range(m)) and (c in range(n)) and (grid[r][c]==1):
                        grid[r][c]=2
                        q.append((r,c))
                        fresh-=1
            time+=1
        
        return time if fresh==0 else -1