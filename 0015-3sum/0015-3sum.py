class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i]  == nums[i-1]:
                continue
            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]
                if cur_sum == 0:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif cur_sum < 0:
                    lo += 1  
                else:
                    hi -= 1  
        return result