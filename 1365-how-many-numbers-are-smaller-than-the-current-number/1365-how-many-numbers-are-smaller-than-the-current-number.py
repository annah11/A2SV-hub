class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        
        smaller_count = {}
        for i, (index, value) in enumerate(sorted_nums):
            if value not in smaller_count:
                smaller_count[value] = i
        
        result = [smaller_count[num] for num in nums]
        return result

