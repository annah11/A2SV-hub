class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d=Counter(nums)
        while d[original]:
            original*=2
        return original