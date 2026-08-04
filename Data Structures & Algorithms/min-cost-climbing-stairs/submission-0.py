class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def rec(i):
            if i>=len(cost):
                return 0
            return cost[i]+min(rec(i+1),rec(i+2))

        return min(rec(0),rec(1))

        