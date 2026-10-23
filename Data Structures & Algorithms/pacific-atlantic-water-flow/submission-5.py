class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])

        def bfs(i,j):
            q = deque([(i,j)])
            seen = set()
            seen.add((i,j))
            pac,alt = False,False

            while q:
                i,j = q.popleft()
                if pac and alt:
                    return True
                for di, dj in ((1,0),(0,1),(-1,0),(0,-1)):
                    r,c=i+di,j+dj
                    if r<0 or c<0:
                        pac = True
                    if r>=n or c >=m:
                        alt = True
                    if 0<=r<n and 0<=c<m and heights[i][j] >= heights[r][c] and (r,c) not in seen:
                        seen.add((r,c))
                        q.append((r,c))
                
                    
            return pac and alt
        res = []
        for i in range(n):
            for j in range(m):
                if bfs(i,j):
                    res.append([i,j])
        return res
        