class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp ={}
        def back(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in dp:
                return dp[amount]
            res = float("inf")
            for c in coins:
                if amount - c >=0:
                    res = min(1+back(amount-c), res)
            dp[amount] = res
            return dp[amount]
        res = back(amount)
        return -1 if res >= float("inf") else res
