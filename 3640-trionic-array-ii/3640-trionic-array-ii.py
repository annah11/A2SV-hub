class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        i = 0
        while i < n - 1:
            while i < n - 1 and nums[i] >= nums[i + 1]:
                i += 1
            start = i
            trionic_sum = 0
            while i < n - 1 and nums[i] < nums[i + 1]:
                trionic_sum += max(0, nums[i])
                i += 1
            peak1 = i
            if peak1 == start or (peak1 + 1 < n and nums[peak1] == nums[peak1 + 1]):
                continue
            
            if nums[peak1 - 1] < 0:
                trionic_sum += nums[peak1 - 1]
            
            while i < n - 1 and nums[i] > nums[i + 1]:
                trionic_sum += nums[i]
                i += 1
            
            valley = i
            
            if valley == peak1 or (valley + 1 < n and nums[valley] == nums[valley + 1]):
                continue
            trionic_sum += nums[valley]
            prefix_sum = 0
            best_prefix = float('-inf')
            while i < n - 1 and nums[i] < nums[i + 1]:
                prefix_sum += nums[i + 1]
                best_prefix = max(best_prefix, prefix_sum)
                i += 1
            peak2 = i
            if peak2 > valley:
                max_sum = max(max_sum, trionic_sum + best_prefix)
                i = valley  
            if start == i:
                i += 1
        return max_sum