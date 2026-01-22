class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        so = False
        ans = 0
        while not so:
            n = len(nums)
            if n == 1:
                return ans
            so = True
            i = 0
            ss = nums[0] + nums[1]
            for x in range(n -1 ):
                if nums[x] + nums[x+1] < ss:
                    ss = nums[x] + nums[x+1]
                    i = x
                if nums[x] > nums[x+1]:
                    so = False
            if not so:
                nums[i] += nums[i+1]
                nums.pop(i+1)
                ans += 1
        return ans
        