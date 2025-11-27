class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        prefix = 0
        best = -10**18
        min_pref = [10**18] * k  
        min_pref[0] = 0          

        for i, x in enumerate(nums):
            prefix += x
            m = (i + 1) % k       
            best = max(best, prefix - min_pref[m])

            min_pref[m] = min(min_pref[m], prefix)

        return best
