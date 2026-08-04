class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        We do not have coin:
            can buy
                profit--
            skip
                profit
        has coin:
            can sell
                profit++ cal
            skip
                profit
        We can backtrack the solution
        
        '''
        dp = {}
        def backtrack(i, has_coin):
            if i >= len(prices):
                return 0
            if (i, has_coin) in dp:
                return dp[(i, has_coin)]
            p1 = backtrack(i + 1, has_coin)
            if not has_coin:
                #not buying
                # p1 = backtrack(i + 1, has_coin)
                #buying
                p2 = backtrack(i + 1, not has_coin) - prices[i]
                dp[(i, has_coin)] =  max(p1, p2)
            else:
                #not selling
                # p3 = backtrack(i + 1, has_coin)
                #elling
                p4 = backtrack(i + 2, not has_coin) + prices[i]
                dp[(i, has_coin)] = max(p1, p4)
            return dp[(i, has_coin)]
            
        return backtrack(0, False)

                
                
