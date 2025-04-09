class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visit = [[False] * cols for _ in range(rows)]
 
        def dfs(r, c):
            if r<0 or r>= rows or c<0 or c >= cols  or grid[r][c] == 0 or  visit[r][c]:
                return 0
            visit[r][c] = True
            cnt =1
            cnt += dfs(r + 1, c)
            cnt +=dfs(r - 1, c)
            cnt +=dfs(r, c + 1)
            cnt += dfs(r, c - 1)
            return cnt
        maxx = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visit[r][c]:
                    maxx =max(maxx,dfs(r, c))
                    
        return maxx

