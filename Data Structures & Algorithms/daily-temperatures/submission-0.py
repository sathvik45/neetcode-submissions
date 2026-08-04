class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        for i in range(0,len(temperatures)-1):
            j=i
            while j<len(temperatures):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break
                j+=1
            if j > len(temperatures)-1:
                res.append(0)
            
        res.append(0)
        return res
        