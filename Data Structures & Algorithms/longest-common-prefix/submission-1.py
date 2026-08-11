class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs))
        print(min_len)
        res = ""
        for i in range(min_len):
            ch = strs[0][i]
            for s in strs:
                if ch != s[i]:
                    return res
            res += ch
        return res