class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # self.quick_sort(nums, 0, len(nums) - 1)
        # hinata = []
        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         hinata.append(nums[i])        
        # return hinata
        nums.sort()
        return [nums[i] for i in range(1, len(nums)) if nums[i] == nums[i - 1]]


    # def quick_sort(self, nums: List[int], left: int, right: int):
    #     if left >= right:
    #         return
    #     pivot_index = self.partition(nums, left, right)
    #     self.quick_sort(nums, left, pivot_index - 1)
    #     self.quick_sort(nums, pivot_index + 1, right)
    

    # def partition(self, nums: List[int], left: int, right: int) -> int:
    #     pivot = nums[right]
    #     i = left - 1
        
    #     for j in range(left, right):
    #         if nums[j] < pivot:
    #             i += 1
    #             nums[i], nums[j] = nums[j], nums[i]
    #     nums[i + 1], nums[right] = nums[right], nums[i + 1]
    #     return i + 1
