class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # d1=defaultdict(int)
        # for i in s1:
        #     d1[i]+=1
        # print(d1)
        d1=[0]*26
        for i in s1:
            d1[ord(i)-ord('a')]+=1
        i=0
        d2=[0]*26
        for j in range(len(s2)):
            d2[ord(s2[j])-ord('a')]+=1
            while j-i+1 > len(s1):
                d2[ord(s2[i])-ord('a')]-=1
                i+=1
            if d2==d1:
                return True
            print(d2)
        return False
        