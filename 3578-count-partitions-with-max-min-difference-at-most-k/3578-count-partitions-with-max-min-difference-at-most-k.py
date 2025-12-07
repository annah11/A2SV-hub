class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        cnt = SortedList()

        dp[0] = 1
        pref[0] = 1
        j = 0

        for i in range(n):
            cnt.add(nums[i])
            # print(cnt)
            while j <= i and cnt[-1] -cnt[0] > k:
                cnt.remove(nums[j])
                j+=1
                # print(cnt)
            dp[i+1] = (pref[i] -(pref[j-1] if j> 0 else 0 )) % MOD
            pref[i+1] = (pref[i] +dp[i+1]) % MOD
        return dp[n]