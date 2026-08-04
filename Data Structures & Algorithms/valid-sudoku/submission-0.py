class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l=0
        for n in [3,6,9]:
            k=0 
            for m in [3,6,9]:
                check=[0]*10
                for i in range(l,n):
                    for j in range(k,m):
                        print(board[i][j],end=' ')
                        if board[i][j] != '.' and check[int(board[i][j])] > 0:
                            print('exit 1')
                            return False
                        if board[i][j] != '.' :
                            check[int(board[i][j])]+=1
                    print()
                k+=3
                print()
            l+=3
        for i in range(9):
            check=[0]*10
            for j in range(9):
                if board[i][j] != '.' and check[int(board[i][j])] > 0:
                    print('exit 2')
                    return False
                if board[i][j] != '.' :
                    check[int(board[i][j])]+=1
                print(board[i][j],end=' ')
            print()
        for i in range(9):
            check=[0]*10
            for j in range(9):
                if board[j][i] != '.' and check[int(board[j][i])] > 0:
                    print('exit 3')
                    return False
                if board[j][i] != '.' :
                    check[int(board[j][i])]+=1
        return True



        
                

        