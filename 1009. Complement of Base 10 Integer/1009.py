class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        n = str(int('1' * len(n)) - int(n))
        return int(n, 2)