class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        hina = 0
        qedmo = 0
        ahun = 1
        for i in range(1,len(nums)):
            if len(nums)<2:
                return 0
            if nums[i] > nums[i-1]:
                ahun +=1
        
            else:
                # qedmo =min( qedmo , ahun)
                # hina = ahun //2

                hina =max(hina,ahun//2)
                hina =max(hina,min(qedmo,ahun))
                qedmo = ahun
                ahun = 1
                print(hina)
        hina =max(hina,ahun//2)
        hina =max(hina,min(qedmo,ahun))
        return hina