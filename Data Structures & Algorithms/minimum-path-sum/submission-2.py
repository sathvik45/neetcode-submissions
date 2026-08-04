class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [float("inf")] * (N + 1)
        dp[N - 1] = 0

        for i in reversed(range(M)):
            for j in reversed(range(N)):
                dp[j] = grid[i][j] + min(dp[j], dp[j + 1])

        return dp[0]