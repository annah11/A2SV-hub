class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zeros = 0
        wind = 0
        start = 0
        for i in range(len(nums)):
            zeros += (nums[i]==0)
            while  zeros >1:
                zeros-=(nums[start]==0)
                start+=1
            wind = max(wind,i-start)
        return wind
