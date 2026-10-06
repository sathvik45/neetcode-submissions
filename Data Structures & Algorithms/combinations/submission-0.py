class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        def back(i,cur):
            if i > n:
                if len(cur) == k:
                    res.append(cur.copy())
                return
            cur.append(i)
            back(i+1, cur)
            cur.pop()
            back(i+1, cur)

        
        back(1,[])
        return res




        