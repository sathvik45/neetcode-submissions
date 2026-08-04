class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0]) 
        directions = ((0, 1), (1, 0))
        seen = set()
        res = 0
        pathways = {(M-1,N-1) : 1}
        print(pathways)
        def dfs(i, j):
            nonlocal res
            if i < 0 or i >= M or j < 0 or j >= N or obstacleGrid[i][j] == 1 :
                return 0
            if i == M - 1 and j == N - 1 and obstacleGrid[i][j] == 0:
                return 1
            if (i,j) in pathways:
                return pathways[(i, j)]
            
            pathways[(i, j)] = 0
            for di, dj in directions:
                r, c = i + di, j + dj
                pathways[(i, j)] += dfs(r, c)
            return pathways[(i,j)]
        
        return dfs(0, 0)
            