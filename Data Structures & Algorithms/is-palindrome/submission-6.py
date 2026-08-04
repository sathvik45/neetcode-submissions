class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for a in s:
            if a.isalnum():
                st += a.lower()
        i, j =0, len(st) -1
        while i < j:
            if st[i] != st[j]:
                return False
            i+=1
            j-=1
        return True