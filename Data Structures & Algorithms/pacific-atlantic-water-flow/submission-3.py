class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def backtrack(i, j, prev):
            nonlocal pac, alt
            if i < 0 or j < 0:
                pac = True
                return
            if i >= len(heights) or j >= len(heights[0]):
                alt = True
                return
            if heights[i][j] > prev or (i, j) in seen:
                return
            
            prev = heights[i][j]
            seen.add((i, j))

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                r, c = i + di, j + dj
                backtrack(r, c, prev)
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                pac, alt = False, False
                seen = set()
                backtrack(i, j, 100000)
                if pac and alt:
                    res.append([i, j])
        return res

            