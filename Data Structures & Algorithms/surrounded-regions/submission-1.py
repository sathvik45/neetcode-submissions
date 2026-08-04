class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n=len(board),len(board[0])
        visited=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            if board[i][j]=='X' or (i,j) in visited:
                return True
            visited.add((i,j))
            res = dfs(i+1,j) and dfs(i-1,j) and dfs(i,j+1) and dfs(i,j-1)
            return res
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    visited=set()
                    if dfs(i,j):
                        for r,c in visited:
                            board[r][c]='X'