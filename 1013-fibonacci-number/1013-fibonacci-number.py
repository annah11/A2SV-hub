class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        fit=0
        ahun=1

        for i in range(2,n+1):
            fit,ahun = ahun,fit+ahun
        return ahun