class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return [0, 1, 1][n]
        F = [0, 1, 1]
        for i in range(3, n + 1):
            F.append(F[-1] + F[-2] + F[-3])
        return F[n]
