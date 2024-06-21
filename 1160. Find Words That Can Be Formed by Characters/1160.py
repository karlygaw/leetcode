class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res1 = 0
        for i in words:
            res = 0
            for j in i:
                if j in chars and i.count(j) <= chars.count(j):
                    res += 1
            if res == len(i):
                res1 += res
        return res1