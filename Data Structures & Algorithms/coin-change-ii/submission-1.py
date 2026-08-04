class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(amount, i):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if (amount, i) in dp:
                return dp[amount, i]
            count = 0
            for c in range(i, len(coins)):
                count += dfs(amount - coins[c], c)
            dp[(amount, i)] = count
            return count
        dfs(amount, 0)
        return dfs(amount, 0)
       

