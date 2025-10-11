class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        # print(cnt)
        count = Counter(power)
        unique = sorted(count.keys())
        n = len(unique)
        
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            cur_d = unique[i-1]
            tot = cur_d * count[cur_d]
            j = i - 1
            while j > 0 and unique[j-1] >= cur_d - 2:
                j -= 1
            skip = dp[i-1]
            take = tot + (dp[j] if j >= 0 else 0)
            
            dp[i] = max(skip, take)
        
        return dp[n]    