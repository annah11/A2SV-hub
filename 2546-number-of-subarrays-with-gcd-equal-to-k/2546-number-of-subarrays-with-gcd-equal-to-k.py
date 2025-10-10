class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            if nums[i]%k != 0:
                continue
            b= 0
            for j in range(i,n):
                if nums[j] %k != 0:
                    break
                b = gcd(nums[j],b)
                if b == k:
                    res+=1
                if b< k:
                    break
        return res