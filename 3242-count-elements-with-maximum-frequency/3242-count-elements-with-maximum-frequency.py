class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # return max(Counter(nums))
        # cnt = Counter(nums)
        # ma_freq = max(cnt.values())
        # return sum (i for i in cnt.values() if i == ma_freq)
            
        return prod(max(Counter(Counter(nums).values()).items()))
        # print(max(Counter(nums).keys()))