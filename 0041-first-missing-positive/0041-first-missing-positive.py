class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # n= len(nums)
        # sor = sorted(nums)

        # for i in range(len(sor)):
        #     if sor[i] != i + 1:
        #         return i + 1
        #     return sor+1
        nums.sort()  
        missing = 1  
        for num in nums:
            if num == missing:
                missing += 1  
        return missing