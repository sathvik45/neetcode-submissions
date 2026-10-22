class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        seen = set()
        q = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    seen.add((i,j))
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh +=1
        
        time = 0
        while q and fresh:
            for _ in range(len(q)):
                i,j = q.popleft()

                for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    r,c = i + di, j + dj
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == 1 and (r,c) not in seen:
                        seen.add((r,c))
                        grid[r][c] = 2
                        fresh-=1
                        q.append((r,c))
            time += 1

        return time if fresh == 0 else -1