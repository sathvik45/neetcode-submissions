class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if not len(digits):
            return []
        res = []
        def back(i, cur):
            if len(cur) >= len(digits):
                res.append(cur)
                return
            
            for j in hashmap[digits[i]]:
                back(i + 1, cur + j)
        back(0,"")
        return res
                
        