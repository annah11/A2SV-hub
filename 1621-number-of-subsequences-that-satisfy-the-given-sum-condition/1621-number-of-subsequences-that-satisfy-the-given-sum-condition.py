class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        count = 0
        MOD = 10 ** 9 + 7
        nums.sort()
        for i in range(len(nums)):
            right = bisect.bisect_right(nums, target - nums[i], 0, i)
            sub = pow(2,right,MOD) - 1
            count += sub
            count += ((pow(2,i - right,MOD) - 1) * sub)
            if nums[i] * 2 <= target:
                count += 1
        count %= MOD
        return count % MOD