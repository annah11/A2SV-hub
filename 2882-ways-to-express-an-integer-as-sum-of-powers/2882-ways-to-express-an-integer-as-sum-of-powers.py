class Solution(object):
    def numberOfWays(self, n, x):
        memo = {}
        MOD = 10**9 + 7

        def dfs(minfelgew, curr):
            if minfelgew == 0:
                return 1
            if minfelgew < 0 or curr ** x > minfelgew:
                return 0
            if (minfelgew, curr) in memo:
                return memo[(minfelgew, curr)]
            
            take = dfs(minfelgew - curr ** x, curr + 1)
            skip = dfs(minfelgew, curr + 1)
            
            memo[(minfelgew, curr)] = (take + skip) % MOD
            return memo[(minfelgew, curr)]

        return dfs(n, 1)
