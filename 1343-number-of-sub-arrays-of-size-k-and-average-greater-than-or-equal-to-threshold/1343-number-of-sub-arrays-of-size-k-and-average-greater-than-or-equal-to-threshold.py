class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res =0
        l=0
        r=k
        _sum = sum(arr[l:k])
        if _sum//k >=threshold:
            res+=1
        while r < len(arr):
            _sum += arr[r]
            _sum -=arr[l]
            l+=1
            r+=1
            if _sum//k >=threshold:
                res+=1
        return res