class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        for i in nums:
            if i not in d.keys():
                d[i] = 0
            d[i]+=1
        print(d)

        arr=[]
        for num,cnt in d.items():
            arr.append([cnt,num])
        arr.sort()

        res=[]
        while k:
            res.append(arr.pop()[1])
            k-=1
        return res
    

        