class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        d1,d2=[0]*26,[0]*26
        for i in range(len(s1)):
            d1[ord(s1[i])-ord('a')]+=1
            d2[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            if d1[i]==d2[i]:
                matches+=1
        i=0
        for j in range(len(s1),len(s2)):
            if matches==26:
                return True
            d2[ord(s2[j])-ord('a')]+=1
            if d2[ord(s2[j])-ord('a')]==1+d1[ord(s2[j])-ord('a')]:
                matches-=1
            elif d2[ord(s2[j])-ord('a')]==d1[ord(s2[j])-ord('a')]:
                matches+=1
            d2[ord(s2[i])-ord('a')]-=1
            if d2[ord(s2[i])-ord('a')]==d1[ord(s2[i])-ord('a')]:
                matches+=1
            elif d2[ord(s2[i])-ord('a')]==d1[ord(s2[i])-ord('a')]-1:
                matches-=1
            i+=1

        return matches==26


