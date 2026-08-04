class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d= int("".join([str(dig) for dig in digits]))
        d += 1
        res = []
        while d:
            res.append(int(d%10))
            d=d//10
        return res[::-1]

        
        