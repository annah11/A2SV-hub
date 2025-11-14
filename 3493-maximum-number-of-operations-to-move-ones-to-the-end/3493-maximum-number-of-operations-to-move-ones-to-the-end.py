class Solution:
    def maxOperations(self, s: str) -> int:
        s += '1'
        s = s.split('0')
        hin = 0
        cntones = 0
        for i in range(len(s) - 1):
            if s[i]:
                cntones += len(s[i])
                hin += cntones
        return hin
