class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums =list(map(str,nums))
        for i in range(len(nums)):
            for j in range(0,len(nums)-i-1):
                if nums[j] + nums[j+1] < nums[j+1] +nums[j]:
                    nums[j] , nums[j+1] = nums[j+1] ,nums[j]
        
        return str(int(''.join(nums)))
