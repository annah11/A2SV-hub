class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot = sum(nums)
        keri = tot % p
        if keri == 0:
            return 0
        prefix = 0
        seen = {0: -1}
        ans = len(nums)
        for i ,num in enumerate(nums):
            prefix = (prefix + num) % p
            # print(prefix)
            target = (prefix-keri)%p
            print(target)
            if target in seen:
                ans = min(ans,i-seen[target])
            seen[prefix] = i

        return ans if len(nums) > ans else -1
