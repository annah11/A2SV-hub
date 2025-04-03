class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i <n:
            pos = nums[i] -1
            if nums[pos]!=nums[i] :
                nums[i],nums[pos] =nums[pos] ,nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i],i+1]
        return []