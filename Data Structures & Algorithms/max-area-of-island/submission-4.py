class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or j <0 or i >= m or j >=n or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            res = 1
            for di, dj in ((0,1),(1,0),(-1,0),(0,-1)):
                r, c = i + di, j + dj
                res += dfs(r, c)
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res
                