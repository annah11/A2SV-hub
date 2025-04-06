class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def helper(coins,amount):
            if amount in memo:
                return memo[amount] 
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            min_coins = float('inf')
            for coin in coins:
                res = helper(coins, amount - coin)
                if res != float('inf'):
                    min_coins = min(min_coins, res + 1)
            memo[amount] = min_coins
            return min_coins
        result =  helper(coins,amount)

        if result == float('inf'):
            return -1
        return result