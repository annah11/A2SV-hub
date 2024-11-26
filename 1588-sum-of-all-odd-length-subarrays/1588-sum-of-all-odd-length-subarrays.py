class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            left = i + 1
            
            right = n - i
            
            total_subarrays = left * right
            
            odd_subarrays = (total_subarrays + 1) // 2
            
            total_sum += arr[i] * odd_subarrays
        return total_sum