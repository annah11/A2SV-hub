class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        ans = 0
        MOD = 10**9 + 7
        for i in s:
            if i == "1":
                cnt= (cnt+1)%MOD
            else:
                cnt =0
            ans =(ans+cnt)%MOD

        return ans