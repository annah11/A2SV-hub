class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        res = 0
        cnt = Counter(nums)
        # print(cnt)
        cur = {}
        for n in nums:
            target = n*2
            left = cur.get(target,0)
            cur[n] = cur.get(n,0) +1
            right = cnt.get(target,0) -cur.get(target,0)
            res += left *right
        return res % mod