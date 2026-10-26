class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m=len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or board[i][j] != "O":
                return
            
            board[i][j] = "#"
            for di,dj in ((1,0),(0,1),(-1,0),(0,-1)):
                dfs(i+di,j + dj)
            
        for r in range(n):
            dfs(r,0)
            dfs(r,m-1)
        for c in range(m):
            dfs(0,c)
            dfs(n-1,c)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

        