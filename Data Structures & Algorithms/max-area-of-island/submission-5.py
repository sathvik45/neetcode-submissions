class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i >=n or j>=m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                r,c = i+ di,j+dj
                res += dfs(r,c)
            return res
        res = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res,dfs(i,j))
        return res
        