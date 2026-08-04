class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        def backtrack(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) in dp:
                return dp[(i, j)]
            res = float("inf")
            if word1[i] == word2[j]:
                res = min(res, backtrack(i + 1, j + 1))
            else:
                res = min(res,1 + backtrack(i, j + 1),1 + backtrack(i + 1, j), 1 + backtrack(i + 1, j + 1) )
            dp[(i, j)] = res
            return res
        return backtrack(0, 0)
                