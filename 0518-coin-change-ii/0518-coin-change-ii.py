class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1]+[0]*amount
        
        for icoin in range(len(coins)-1,-1,-1):
            for i in range(amount+1):
                if i >= coins[icoin]:
                    dp[i] = dp[i-coins[icoin]] + dp[i]
                else:
                    dp[i] = dp[i]
                    
        return dp[amount]
