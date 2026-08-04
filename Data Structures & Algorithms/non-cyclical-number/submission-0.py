class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n!= 1:
            res = 0
            if n in seen:
                return False
            seen.add(n)
            while n:
                rem = int(n % 10)
                res += rem**2
                n = n//10
            n = res
        return True

        