class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = {}
        def dfs(i, j, prev):
            
            if i < 0 or j < 0 or i >= M or j >=N or prev >= matrix[i][j]:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                r, c = i + di, j + dj
                res = max(res, 1 + dfs(r, c, matrix[i][j]))
            dp[(i, j)] = res

            return res
    
        for i in range(M):
            for j in range(N):
                dfs(i, j, -1)
        return max(dp.values())