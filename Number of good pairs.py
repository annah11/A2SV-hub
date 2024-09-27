class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq = {}
        good_pairs = 0
        
        for num in nums:
            if num in freq:
                good_pairs += freq[num]
            freq[num] = freq.get(num, 0) + 1
        
        return good_pairs
