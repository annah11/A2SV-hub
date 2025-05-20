class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        xor2= 0
        len1 =len(nums1)
        len2 = len(nums2)
        for n1 in nums1:
            xor1 ^=n1
        for n2 in nums2:
            xor2 ^=n2
        res = (xor1 if len2 % 2 != 0 else 0) ^ (xor2 if len1 % 2 != 0 else 0)

        return res
        