class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        cnt = Counter(nums)
        # print(cnt.keys)
        for i,v in cnt.items():
            if v == n:
                return i