class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c=[-1]*len(cost)
        def rec(i):
            if i>=len(cost):
                return 0
            if c[i]!=-1:
                return c[i]
            c[i]=cost[i]+min(rec(i+1),rec(i+2))
            return c[i]

        return min(rec(0),rec(1))

        