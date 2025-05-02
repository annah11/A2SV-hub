class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diff = [0] * (len(nums)+1)
        total=0 
        res= 0
        for i in range(len(nums)):
            while diff[i] +total < nums[i]:
                res+=1
                if res >len(queries):
                    return -1
                l,r,val = queries[res-1]
                if r>=i:
                    diff[max(l,i)]+=val
                    diff[r+1] -=val
            total +=diff[i]
        return res
