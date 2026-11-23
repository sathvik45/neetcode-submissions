class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i,has_coin):
            if (i,has_coin) in dp:
                return dp[(i,has_coin)] 
            if i >= len(prices):
                return 0
            rest = dfs(i+1,has_coin)
            if not has_coin:
                buying = dfs(i+1,not has_coin) - prices[i]
                rest = max(rest,buying)
            if has_coin:
                selling = prices[i] + dfs(i+2,not has_coin)
                rest = max(rest,selling)
            dp[(i,has_coin)] = rest
            return rest
        return dfs(0,False)