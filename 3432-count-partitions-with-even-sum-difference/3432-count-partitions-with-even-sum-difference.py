class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n-1):
            if (sum(nums[0:i+1])-sum(nums[i+1:n]) )% 2==0 :
                cnt +=1
            # print(sum(nums[0:i+1])-sum(nums[i+1:n]))
            # print(nums[0:i+1])
            # print(nums[i+1:n])
        return cnt