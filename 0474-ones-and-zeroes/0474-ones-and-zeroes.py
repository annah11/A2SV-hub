class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}
        for s in strs:
            ones = 0
            zeroes = 0
            for ch in s:
                if ch == "0":
                    zeroes += 1
                else:
                    ones += 1
            newdp = {}
            for k, v in dp.items():
                pre, pon = k
                nwzer, nwone = pre + zeroes, pon + ones
                if nwzer <= m and nwone <= n:
                    if (nwzer, nwone) not in dp:
                        newdp[(nwzer, nwone)] = v + 1

                    elif dp[(nwzer, nwone)] < v + 1:
                        newdp[(nwzer, nwone)] = v + 1
            dp.update(newdp)
        return max(dp.values())