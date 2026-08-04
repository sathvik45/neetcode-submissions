#we can backtrack from starting letter and dfs on 4 directins, store the seen variable
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(i, j, idx):
            # nonlocal cur
            # if cur == word:
            #     return True
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or word[idx] != board[i][j] or ((i,j) in seen):
                return False
            
            
            seen.add((i,j))
            res = dfs(i+1,j,idx + 1) or dfs(i, j+1, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j - 1, idx + 1)
            seen.remove((i,j))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                seen =set()
                cur = ""
                if dfs(r, c, 0):
                    return True
        return False
        # print(dfs(2,0,0))




        