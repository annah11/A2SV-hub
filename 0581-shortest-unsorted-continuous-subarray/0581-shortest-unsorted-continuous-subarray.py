class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = -1, -1
        
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                left = i - 1
                break
        
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                right = i + 1
                break
        
        if left == -1 and right == -1:
            return 0
        
        subarray_min = min(nums[left:right+1])
        subarray_max = max(nums[left:right+1])
        
        while left >= 0 and nums[left] > subarray_min:
            left -= 1
        
        while right < n and nums[right] < subarray_max:
            right += 1
        
        return right - left - 1
