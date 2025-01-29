class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x,n):
            if n == 0:
                return 1
            r = rec (x,n//2)
            if n % 2 == 0:
               return r * r
            else:
               return r * r * x

        result = rec(x,abs(n))
        return result if n >=0 else 1 /result


