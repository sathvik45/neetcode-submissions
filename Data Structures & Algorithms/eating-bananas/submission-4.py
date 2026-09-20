class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = float("inf")
        while l <= r:
            mid = (l+r)//2
            cal = 0
            for pile in piles:
                cal+= math.ceil(pile/mid)
            if cal > h:
                l = mid + 1
            elif cal <= h:
                r = mid - 1
                res = min(res, mid)
        
        return res
            
