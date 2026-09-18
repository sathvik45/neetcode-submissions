class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dt = {}
        for ele in t:
            dt[ele] = dt.get(ele,0) + 1
        ds = {}
        res = ""
        need = len(dt)
        l,r = 0,0
        match = 0 
        res = [-1,-1]
        reslen=float("inf")
        for r in range(len(s)):
            ds[s[r]] = ds.get(s[r],0) + 1
            if dt.get(s[r],0) == ds[s[r]]:
                match += 1
            while match == need:
                if r-l+1 < reslen:
                    res = [l,r]
                    reslen = r-l+1
                ds[s[l]] -= 1
                if s[l] in dt and ds[s[l]] < dt[s[l]]:
                    match -=1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float("inf") else ""
            



        