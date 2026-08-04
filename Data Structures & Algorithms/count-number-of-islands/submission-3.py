class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(i, j):
            if  i < 0 or j <0 or i >= m or j >= n or grid[i][j] == "0" or (i,j) in seen:
                return 
            seen.add((i, j))

            for di, dj in ((1,0), (0,1), (-1,0), (0, -1)):
                r, c = i + di, j + dj
                dfs(r, c)
        res = 0
        for i in range(m):
            for j in range(n):
                
                if (i, j) not in seen and grid[i][j] == "1":
                    print(i,j,seen)
                    dfs(i, j)
                    res += 1
        return res
        