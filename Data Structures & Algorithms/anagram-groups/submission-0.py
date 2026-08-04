class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for st in strs:
            sorted_st="".join(sorted(st))
            if sorted_st not in d.keys():   
                d[sorted_st]= list()
                d[sorted_st].append(st)
            else:
                d[sorted_st].append(st)
            
        return list(d.values())

