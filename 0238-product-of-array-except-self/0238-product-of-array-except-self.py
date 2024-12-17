class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult =1
        r_mult =1
        n = len(nums)
        l_arr =[0]*n
        a_arr = [0]*n
        for i in range(n):
            j = -i-1
            l_arr[i] = l_mult
            a_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult*= nums[j]
        return [l*r for l,r in zip(l_arr,a_arr)]
  