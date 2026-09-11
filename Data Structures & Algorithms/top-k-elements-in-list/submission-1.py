class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums:
            dp[num] = dp.get(num,0) + 1
        
        arr = []
        for ele,cnt in dp.items():
            arr.append([cnt,ele])
        arr.sort()
        res = []
        while k:
            res.append(arr.pop()[1])
            k-=1
        return res