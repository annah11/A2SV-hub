class Solution:
    def maxArea(self, height: List[int]) -> int:
        n= len(height)
        l,r = 0,n-1
        ans = 0
        while l<r:
            dis = r -l  
            area = min(height[l],height[r]) * dis
            ans = max(area,ans)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return ans


        