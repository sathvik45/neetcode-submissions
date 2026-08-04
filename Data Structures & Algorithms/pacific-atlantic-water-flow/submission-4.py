class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, alt = deque(), deque()
        for i in range(R):
            pac.append((i, 0))
            alt.append((i,C - 1))
        for j in range(C):
            pac.append((0, j))
            alt.append((R - 1, j))
        p, a = set(), set()

        def BFS(ocean, seen):
            while ocean:
                for _ in range(len(ocean)):
                    i, j = ocean.popleft()
                    seen.add((i, j))
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        r, c = i + di, j + dj
                        if 0 <= r < R and 0 <= c < C and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                            seen.add((r, c))
                            ocean.append((r, c))
        
        BFS(pac, p)
        BFS(alt, a)
        res= []
        for ele in p:
            if ele in a:
                res.append(list(ele))
        return res




