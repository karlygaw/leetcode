class Solution:
    def romanToInt(self, s: str) -> int:
        romanempire = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        res = 0
        for i in range(len(s)-1):
            if romanempire[s[i]] < romanempire[s[i+1]]:
                res -= romanempire[s[i]]
            else:
                res += romanempire[s[i]]
        return res+romanempire[s[-1]]
