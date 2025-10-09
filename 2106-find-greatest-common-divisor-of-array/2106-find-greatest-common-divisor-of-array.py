class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = 0
        for i in range(len(nums)):
            ans = gcd(nums[0],nums[len(nums)-1])
        # print(i)
        return ans