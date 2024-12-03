class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0 
            curSum += n
            maxsub = max(maxsub, curSum)
        return maxsub