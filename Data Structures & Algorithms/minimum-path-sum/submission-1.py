class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # res = flaot('inf')
        M, N = len(grid), len(grid[0])
        dp = {(M - 1 , N -1): grid[M - 1][N - 1]}
        def dfs(i, j):
            if i == M or j == N :
                return float('inf')
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)
            