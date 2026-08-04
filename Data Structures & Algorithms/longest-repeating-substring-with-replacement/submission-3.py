class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        freq=defaultdict(int)
        res=0
        for j in range(len(s)):
            freq[s[j]]+=1
            if j-i+1 - max(freq.values())<=k:
                res=max(res,j-i+1)
            else:
                while j-i+1 -max(freq.values())>k:
                    freq[s[i]]-=1
                    i+=1
                
        return res

        