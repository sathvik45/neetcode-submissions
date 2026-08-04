class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        for i in range(1,len(height)-1):
            l=max(height[:i])
            r=max(height[i+1:])
            cal=min(l,r)-height[i]
            if cal>0:
                res+=cal
        return res