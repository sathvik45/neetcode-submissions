class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]

            res=0
            for di, dj in [[1, 0], [0, 1]]:
                res +=dfs(i + di, j + dj)
                dp[i][j] = res
            return res
        return dfs(0, 0)
