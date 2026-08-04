class Solution:
    def climbStairs(self, n: int) -> int:
        steps=[-1]*n
        # steps[1]=1
        # steps[2]=2
        def rec(step):
            if n==step:
                return 1
            if step>n:
                return 0
            if steps[step]!= -1:
                return steps[step]
            steps[step]=rec(step+1)+rec(step+2)
            return steps[step]
        return rec(0)
            
            
        