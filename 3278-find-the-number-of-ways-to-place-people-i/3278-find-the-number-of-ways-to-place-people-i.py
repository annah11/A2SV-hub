class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        
        n = len(points)
        ans = 0
        
        for i in range(n - 1):
            xA, yA = points[i]
            max_y = float('-inf')
            for j in range(i + 1, n):
                _, yB = points[j]
                if yB <= yA and yB > max_y:
                    ans += 1
                    max_y = yB
        
        return ans