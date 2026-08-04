class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #2 actions buy and sell
        # in a partical day he has 4 options he can but or ignore, sell or ignore
        # if he has a coin he can not buy so sell or ignore
        # id he dont have a coin he can not sell, he can only but or ignore
        #we have to have a flag which will help us if he has a coin or not
        dp = {}
        def backtrack(i, has_coin):
            if i >= len(prices):
                return 0
            if (i, has_coin) in dp:
                return dp[(i , has_coin )]
            if not has_coin:
                dp[(i, False)] = max(backtrack(i + 1, True) - prices[i], backtrack(i + 1, False))
                return dp[(i, False)]
                
            else:
                dp[(i, True)] = max(backtrack(i + 2, False) + prices[i], backtrack(i + 1, True))
                return dp[(i, True)]
        
        return backtrack(0, False)
                
            
                