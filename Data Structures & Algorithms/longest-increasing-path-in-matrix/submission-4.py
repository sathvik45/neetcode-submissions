from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = 1  # path includes current cell
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                r, c = i + di, j + dj
                if 0 <= r < M and 0 <= c < N and matrix[r][c] > matrix[i][j]:
                    res = max(res, 1 + dfs(r, c))
            
            dp[(i, j)] = res
            return res

        return max(dfs(i, j) for i in range(M) for j in range(N))
