class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        res=0
        lmin=prices[0]
        while i < len(prices):
            res=max(res,prices[i]-lmin)
            lmin=min(lmin,prices[i])
            i+=1
        return res
            

        