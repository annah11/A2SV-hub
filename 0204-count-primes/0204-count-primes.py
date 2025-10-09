class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n==1:
            return 0
        nums = [True] * (n)
        
        nums[0] = nums[1] = False

        for i in range(2,n):
            if nums[i] == True:
                for k in range(i*i,n,i):
                    nums[k] = False
        cnt = 0
        # print(nums)
        for bl in nums:
            if bl:
                cnt+=1

        return cnt
            