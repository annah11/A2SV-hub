class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maxArea = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i + 1 , n):
                bottom = (max(bottomLeft[i][0],bottomLeft[j][0]) , max(bottomLeft[i][1],bottomLeft[j][1]))
                top = (min(topRight[i][0],topRight[j][0]) , min(topRight[i][1],topRight[j][1]))
                if top[0] - bottom[0] < 0 or  top[1] - bottom[1] < 0:continue
                a = min (abs(top[0] - bottom[0]) , abs(top[1] - bottom[1]))
                maxArea = max(maxArea  , a)
        return maxArea**2