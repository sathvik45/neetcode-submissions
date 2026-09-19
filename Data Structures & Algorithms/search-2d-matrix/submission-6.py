class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bot = 0, len(matrix) - 1
        while top <= bot:
            idx = int((top+bot)/2)
            if target > matrix[idx][0]:
                top = idx + 1
            elif target < matrix[idx][0]:
                bot = idx - 1
            else:
                break
        top = (top+bot)//2
        l,r = 0,len(matrix[0]) -1
        while l <= r:
            idx =int((l+r)/2)
            if target == matrix[top][idx]:
                return True
            elif target < matrix[top][idx]:
                r = idx -1
            else:
                l = idx + 1
        return False
