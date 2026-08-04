class Solution:
    def climbStairs(self, n: int) -> int:
        def rec(step):
            if n==step:
                return 1
            if step>n:
                return 0
            return rec(step+1)+rec(step+2)
        return rec(0)
            
            
        