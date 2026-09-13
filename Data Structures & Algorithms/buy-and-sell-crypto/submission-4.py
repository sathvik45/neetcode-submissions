class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        min_p = float("inf")
        for i in range(n):
            min_p = min(min_p,prices[i])
            res = max(res, prices[i] - min_p)
        return res