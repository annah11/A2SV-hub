class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        remainder_count = {0: 1} 
        count = 0
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k           
            if remainder < 0:
                remainder += k
            if remainder in remainder_count:
                count += remainder_count[remainder]
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        return count
