class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int),defaultdict(int)
        for s1 in s:
            d1[s1] +=1
        for t1 in t:
            d2[t1] +=1
        if d1 == d2:
            return True
        return False
