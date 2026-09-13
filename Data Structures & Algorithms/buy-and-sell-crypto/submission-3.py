class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        for i in range(n):
            res = max(res, max(prices[i:])- prices[i])
        return res