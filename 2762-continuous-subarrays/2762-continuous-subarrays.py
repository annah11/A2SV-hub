class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for start in range(n):
            current_min = current_max = nums[start]
            for end in range(start, n):
                current_min = min(current_min, nums[end])
                current_max = max(current_max, nums[end])
                if current_max - current_min <= 2:
                    count += 1
                else:
                    break
        return count