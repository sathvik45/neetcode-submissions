class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        def dfs(i, j):

            if i < 0 or j < 0 or i > R -1 or j > C-1:
                return 
            if board[i][j] != 'O':
                return 
            board[i][j] = "#"
            
            for di, dj in ((1, 0),(-1, 0), (0, 1), (0, -1)):
                r, c = i + di, j + dj
                dfs(r, c)

        for i in range(R):
            dfs(i, 0)
            dfs(i, C - 1)
        for j in range(C):
            dfs(0, j)
            dfs(R -1, j)

        print(board)
        for i in range(R):
            for j in range(C):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                if board[i][j] == "#":
                    board[i][j] = "O"