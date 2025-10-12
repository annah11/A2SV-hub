MOD = 10**9 + 7

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(remaining_positions, required_bits, current_index, carry):
            if remaining_positions < 0 or required_bits < 0 or remaining_positions + carry.bit_count() < required_bits:
                return 0
            if remaining_positions == 0:
                if required_bits == carry.bit_count():
                    return 1
                else:
                    return 0
            if current_index >= len(nums):
                return 0
                
            result = 0
            for count in range(remaining_positions + 1):
                combinatorial_factor = math.comb(remaining_positions, count) * pow(nums[current_index], count, MOD) % MOD
                
                new_sum = carry + count
                new_carry = new_sum // 2
                new_least_significant_bit = new_sum % 2
                
                result += combinatorial_factor * dp(
                    remaining_positions - count,
                    required_bits - new_least_significant_bit,
                    current_index + 1,
                    new_carry
                )
            return result % MOD
        
        return dp(m, k, 0, 0)
        