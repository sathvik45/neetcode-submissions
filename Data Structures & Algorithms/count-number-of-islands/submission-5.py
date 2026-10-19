class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # seen = set()
        res = 0
        n,m = len(grid),len(grid[0])
        def dfs(i,j):
            if i < 0 or j < 0 or i >=n or j >= m  or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                r,c = i+di, j+dj
                dfs(r,c)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
        return res
                    
        