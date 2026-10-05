class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or (i,j) in seen or board[i][j] != word[idx]:
                return False
            seen.add((i,j))
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)
            seen.remove((i,j))
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        