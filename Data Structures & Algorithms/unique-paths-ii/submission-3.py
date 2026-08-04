class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * N
        dp[0] = 1

        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]
        
        return dp[N - 1]
