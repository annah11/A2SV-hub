class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
     
        pair =0
        cur =0
        cnt = Counter(nums)
        for i in cnt.values():
            pair += i//2
            cur += i%2
        return [pair,cur]