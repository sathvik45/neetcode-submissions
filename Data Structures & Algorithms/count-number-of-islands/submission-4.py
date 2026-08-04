class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def BFS(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = "0"
            while q:
                r, c = q.popleft()
                for di, dj in ((0,1), (1,0), (-1,0), (0,-1)):
                    row, col = r + di, c + dj
                    if (0 <= row < m) and (0 <= col < n) and grid[row][col] == "1":
                        q.append((row, col))
                        grid[row][col] = "0"
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    BFS(i, j)
                    res += 1
        return res 