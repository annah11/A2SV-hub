class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr =float("-inf")
        ans = 0
        for x in nums:
            v = max(x - k, curr + 1)
            if v <= x + k:
                ans += 1
                curr = v
        return ans