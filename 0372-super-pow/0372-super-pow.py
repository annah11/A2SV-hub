class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        naru = 1
        for i in b:
            naru = (pow(naru, 10, mod) * pow(a, i, mod)) % mod
        return naru