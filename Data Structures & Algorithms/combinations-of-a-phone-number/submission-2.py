class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {
            '2' : "abc",
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : "wxyz"
        }
        res = []
        seen = set()
        def back(i,cur):
            if i == len(digits):
                res.append(cur)
                return
            for c in hashmap[digits[i]]:
                back(i+1,cur+c)

        if digits:
            back(0,"")
        return res