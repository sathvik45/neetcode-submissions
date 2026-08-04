class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pac,alt=False,False
        directions=[[0,-1],[0,1],[1,0],[-1,0]]
        res=[]
        def dfs(i,j,prev):
            nonlocal pac,alt,visited
            if i<0 or j<0:
                pac=True
                return
            if i>=m or j>=n:
                alt=True
                return
            if heights[i][j]>prev:
                return
            if (i,j) in visited:
                return
            prev=heights[i][j]
            visited.add((i,j))
            for di,dj in directions:
                r,c=i+di,j+dj
                # if heights[r][c]<=prev:
                dfs(r,c,prev)
                if alt and pac:
                    break

        for i in range(m):
            for j in range(n):
                pac,alt=False,False
                visited=set()
                dfs(i,j,float("inf"))
                if pac and alt:
                    res.append([i,j])

        # dfs(0,0,0)
        # print(pac,alt)
        return res

            