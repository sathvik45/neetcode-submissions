class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(i, j):
            nonlocal cnt
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0 or (i, j) in seen:
                return

            cnt += 1
            seen.add((i, j))
            for di, dj in directions:
                r, c = i + di, j + dj
                dfs(r, c)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt = 0
                dfs(i, j)
                # print(i,j,cnt,res)
                res = max(res, cnt)
        return res


            

        