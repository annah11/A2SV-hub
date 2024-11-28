class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c_sum =sum(nums[:k])
        max_sum = c_sum

        for i in range(k,len(nums)):
            c_sum += nums[i] - nums[i-k]
            max_sum =max(max_sum,c_sum)
        return max_sum/k