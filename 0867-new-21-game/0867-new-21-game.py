class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * (n + 1)   
        dp[0] = 1.0
        windowSum = 1.0       
        res = 0.0

        for i in range(1, n + 1):
            dp[i] = windowSum / maxPts
            if i < k:
                windowSum += dp[i]       
            else:
                res += dp[i]          
            if i - maxPts >= 0:
                windowSum -= dp[i - maxPts]

        return res
        