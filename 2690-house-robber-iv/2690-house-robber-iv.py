class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        
        def can_rob(mid):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        
        while left < right:
            mid = (left + right) // 2
            if can_rob(mid):
                right = mid
            else:
                left = mid + 1

        return left
