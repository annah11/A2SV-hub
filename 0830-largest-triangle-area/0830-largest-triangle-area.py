class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        return max(
        abs(b1*(h2-h3)+b2*(h3-h1) + b3*(h1-h2))/2
        for (b1,h1),(b2,h2),(b3,h3) in  itertools.combinations(points,3)
        )
           