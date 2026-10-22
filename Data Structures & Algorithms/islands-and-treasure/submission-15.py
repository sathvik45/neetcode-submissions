class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        n, m = len(grid), len(grid[0])
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen.add((i,j))
                    q.append((i,j))
        
        
        step = 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                grid[i][j] = step
                for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    r, c = i + di, j + dj
                    if 0 <= r < n and 0 <= c < m and (r,c) not in seen and grid[r][c] != -1:    
                        seen.add((r,c))
                        q.append((r,c))

            step +=1
         


        