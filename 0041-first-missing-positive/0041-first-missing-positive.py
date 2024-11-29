class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n+1
        # nums.sort()  
        # missing = 1  
        # for num in nums:
        #     if num == missing:
        #         missing += 1  
        # return missing