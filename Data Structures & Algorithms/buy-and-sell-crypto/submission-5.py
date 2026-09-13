class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_p = float("inf")
        for p in prices:
            min_p = min(min_p,p)
            res = max(res,p-min_p)
        return res
