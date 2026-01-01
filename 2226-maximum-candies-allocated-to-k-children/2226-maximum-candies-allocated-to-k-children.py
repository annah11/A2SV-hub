class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        ans = 0
        l,r = 1,max(candies)
        while l<= r:
            cnt = 0
            mid =l+(r-l)//2
            for candy in candies:
                cnt += candy//mid
            if cnt >=k:
                ans = mid
                l = mid+1
            else:
                r= mid-1
        return ans