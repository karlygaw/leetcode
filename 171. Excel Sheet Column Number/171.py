class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = len(columnTitle)
        lens = 1
        res = 0
        for i in columnTitle:
            res += (ord(i) - 64) * pow(26, num-lens)
            lens += 1
        return res