class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0 
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
        
        # dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        # for i in range(len(coins)+1):
        #     dp[i][0] =1
        # for i in range(1,len(coins)+1):
        #     for j in range(1,amount+1):
        #         if coins[i-1] >j:
        #             dp[i][j]=dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        # return dp[len(coins)][amount]