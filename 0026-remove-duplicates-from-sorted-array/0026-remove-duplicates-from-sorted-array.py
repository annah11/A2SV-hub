class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newArray = sorted(set(nums)) 
        for i in range(len(newArray)):
            nums[i] = newArray[i]
        
        return len(newArray)
