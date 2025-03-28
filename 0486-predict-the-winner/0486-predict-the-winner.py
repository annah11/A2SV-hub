class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dp(i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))
        
        return dp(0, len(nums) - 1) >= 0
                