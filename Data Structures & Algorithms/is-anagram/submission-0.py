class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1,d2={},{}
        for i in s:
            if i not in d1.keys():
                d1[i]=0
            else:
                d1[i]+=1
        for i in t:
            if i not in d2.keys():
                d2[i]=0
            else:
                d2[i]+=1
        if d1==d2:
            return True
        return False    



        