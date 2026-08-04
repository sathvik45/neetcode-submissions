class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        rotated = [[0 for _ in range(n)]  for _ in range(m) ]
        # print(matrix)
        # print(rotated)
        for i in range(m):
            for j in range(n):
                rotated[j][n - 1 - i] = matrix[i][j]
        for i in range(m):
            for j in range(n):
                matrix[i][j] = rotated[i][j]