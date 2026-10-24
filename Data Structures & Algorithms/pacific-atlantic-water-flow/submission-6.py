class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac, alt = set(), set()

        def dfs(i,j,seen,prev):
            if i < 0  or j < 0 or i >= n or j >= m or (i,j) in seen or heights[i][j] < prev:
                return
            seen.add((i,j))
            prev = heights[i][j]
            for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                r,c = i + di, j + dj
                dfs(r,c,seen,prev)
        
        for c in range(m):
            dfs(0,c,pac,heights[0][c])
            dfs(n-1,c,alt,heights[n-1][c])
        
        for r in range(n):
            dfs(r,0,pac,heights[r][0])
            dfs(r,m-1,alt,heights[r][m-1])
        res = []
        for i in range(n):
            for j in range(m):
                if (i,j) in pac and (i,j) in alt:
                    res.append([i,j])
        return res