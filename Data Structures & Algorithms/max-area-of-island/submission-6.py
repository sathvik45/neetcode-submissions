class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def bfs(i,j):
            q = deque([(i,j)])
            grid[i][j] = 0
            area = 1
            while q:
                for _ in range(len(q)):
                    i,j = q.popleft()
                    for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                        r,c = i+ di, j+dj
                        if 0<=r<n and 0<=c<m and grid[r][c] == 1:
                            area += 1
                            grid[r][c] = 0
                            q.append((r,c))
            return area
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res,bfs(i,j))
        return res
