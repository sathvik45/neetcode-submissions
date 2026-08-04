class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            if n<0:
                res = res/x
            else:
                res = res*x
        return res