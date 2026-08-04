class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        c=0
        res=0
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
                return
            nonlocal c
            c+=1
            grid[i][j]=0
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    c=0
                    dfs(i,j)
                    res=max(res,c)
        return res
        