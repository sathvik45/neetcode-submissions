class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=defaultdict(int)
        for i in s1:
            d1[i]+=1

        for i in range(len(s2)):
            d2=defaultdict(int)
            for j in range(i,len(s2)):
                d2[s2[j]]+=1
                if d1==d2:
                    return True
        return False


        