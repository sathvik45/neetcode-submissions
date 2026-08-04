class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSum(n):
            res = 0
            while n:
                res += int(n%10)**2
                n = n//10
            return res
        
        slow, fast = n, getSum(n)

        while slow!=fast:
            fast = getSum(fast)
            fast = getSum(fast)
            slow = getSum(slow)
        if fast == 1:
            return True
        return False