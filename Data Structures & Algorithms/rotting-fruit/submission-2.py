class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q =deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        time = 0
        while q:
            flag = False
            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    r, c = i + di, j + dj
                    if (r in range(len(grid))) and c in range(len(grid[0])) and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        q.append((r, c))
                        flag = True
            if flag:
                time += 1
        
        return time if fresh == 0 else -1
            
                