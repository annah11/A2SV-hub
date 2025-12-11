class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        maxx = [-1] * (n + 1)   
        minx = [n + 1] * (n + 1) 
        maxy = [-1] * (n + 1)  
        miny = [n + 1] * (n + 1) 
        for x, y in buildings:
            maxx[y] = max(maxx[y], x)
            minx[y] = min(minx[y], x)
            maxy[x] = max(maxy[x], y)
            miny[x] = min(miny[x], y)
        
        res = 0
        for x, y in buildings:
            row = (minx[y] < x < maxx[y])
            col = (miny[x] < y < maxy[x])
            if row and col:
                res += 1
        return res