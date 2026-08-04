class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(i, j):
            if  i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return 
            grid[i][j] = "0"
            for di, dj in directions:
                r, c = i + di, j + dj
                dfs(r, c)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res+=1
        return res

