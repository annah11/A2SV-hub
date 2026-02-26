class Solution:
    def numSteps(self, s: str) -> int:
        N = len(s)

        op = 0
        carry = 0
        for i in range(N - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                op += 2
                carry = 1
            else:
                op += 1

        return op + carry