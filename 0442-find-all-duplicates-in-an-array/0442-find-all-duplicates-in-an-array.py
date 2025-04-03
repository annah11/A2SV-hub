class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i< n:
            pos = nums[i] -1
            if nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i] , nums[pos]
            else :
                i +=1
        return [nums[i] for i in range(len(nums)) if nums[i] != i + 1]

