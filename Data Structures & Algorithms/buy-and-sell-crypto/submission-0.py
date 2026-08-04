class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        res=0
        while i < len(prices)-1:
            j=i+1
            while j < len(prices):
                res=max(res,prices[j]-prices[i])
                j+=1
            i+=1
        return res

        