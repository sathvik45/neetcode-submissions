class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber:
            columnNumber -= 1
            rem = int(columnNumber % 26)
            print(rem)
            res.append(chr(ord('A') + rem ))
            columnNumber = columnNumber // 26
            print(columnNumber)
        return "".join(reversed(res))

