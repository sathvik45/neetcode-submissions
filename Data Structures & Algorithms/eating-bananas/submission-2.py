class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        LL=1
        UL=piles[-1]
        # for k in range(1,UL+1):
        #     H=0
        #     for p in piles:
        #         H+=math.ceil(p/k)
        #     if H<=h:
        #         return k
        res=0
        while LL<=UL:
            k=(LL+UL)//2
            H=0
            for p in piles:
                H+=math.ceil(float(p)/k)
            if H > h:
                LL=k+1
            else :
                res=k
                UL=k-1
        return res
        
