class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        self.quick_sort(nums, 0, len(nums) - 1)
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)

    def quick_sort(self, nums: List[int], left: int, right: int):
        if left >= right:
            return
        
        pivot_index = self.partition(nums, left, right)
        self.quick_sort(nums, left, pivot_index - 1)
        self.quick_sort(nums, pivot_index + 1, right)

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        i = left - 1
        
        for j in range(left, right):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
