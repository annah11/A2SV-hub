class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        old = 0
        for i in nums:
            old = (old*2 +i)%5
            ans.append(old == 0)
        return ans