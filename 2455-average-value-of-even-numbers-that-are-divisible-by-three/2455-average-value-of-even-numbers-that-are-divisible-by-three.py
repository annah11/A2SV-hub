class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = []
        fin = 0
        for i in nums:
            if i % 2 == 0 and i %3 == 0:
                ans.append(i)
        if ans:
            return sum(ans)//len(ans)
        return 0
