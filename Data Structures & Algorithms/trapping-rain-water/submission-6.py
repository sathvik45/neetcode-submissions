class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffix = [0]*n
        prefix = [0]*n
        suffix[0] = height[0]
        prefix[n - 1] = height[n -1]
        res = 0
        for i in range(1,len(height)):
            suffix[i] = max(suffix[i-1] , height[i])
        
        for i in range(len(height) - 2,-1,-1):
            prefix[i] = max(prefix[i + 1], height[i])
        
        # print(suffix)
        # print(prefix)
        for i in range(n):
            res += min(suffix[i],prefix[i]) - height[i]
        return res

        