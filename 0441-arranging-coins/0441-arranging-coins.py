class Solution:
    def arrangeCoins(self, n: int) -> int:
    
        cnt = 0
        while n > cnt:
            cnt += 1
            n = n - cnt
        
        return cnt