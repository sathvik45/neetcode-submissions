class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n=len(grid),len(grid[0])
        from collections import deque
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        
        
        def bfs(i,j):
            que=deque()
            que.append((i,j))
            seen=set()
            seen.add((i,j))
        
            steps=0
            while que:
                for q in range(len(que)):
                    i,j=que.popleft()
                    
                    for di,dj in directions:
                        r,c=i+di,j+dj
                        if r<0 or c<0 or r>=m or c>=n or grid[r][c]==-1 or (r,c) in seen:
                            continue
                        elif grid[r][c]==0:
                            return steps+1
                        else:
                            que.append((r,c))
                            seen.add((r,c))
                steps+=1
            return 2147483647
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2147483647:
                    grid[i][j]=bfs(i,j)
        # print(bfs(0,0))