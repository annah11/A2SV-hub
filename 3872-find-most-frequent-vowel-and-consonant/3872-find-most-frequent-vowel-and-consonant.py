class Solution:
    def maxFreqSum(self, s: str) -> int:
        vol ="aeiou"
        freq= Counter(s)
        mvol = 0
        mcn =0
        for ch,cnt in freq.items():
            if ch in vol:
                mvol=max(mvol,cnt)
            else:
                mcn = max(mcn,cnt)
            # print(cn_cnt)
        
        return  (mcn + mvol)