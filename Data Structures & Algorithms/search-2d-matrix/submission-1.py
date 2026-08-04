class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl,rr,cl=0,len(matrix)-1,0
        while rl <= rr:
            m=(rl+rr)//2
            if matrix[m][-1] < target:
                rl=m+1
            elif matrix[m][0] > target:
                rr=m-1
            else:
                break
        # if not (rl <= rr):
        #     return False
        M=(rl+rr)//2
        cr=len(matrix[M])-1
        while cl <= cr:
            m=(cl+cr)//2
            if matrix[M][m] < target:
                cl=m+1
            elif matrix[M][m] > target:
                cr=m-1
            else:
                return True
        return False

        