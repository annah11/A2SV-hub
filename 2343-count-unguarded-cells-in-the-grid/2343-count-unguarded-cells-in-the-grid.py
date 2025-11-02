class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]        
        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2
        for r, c in guards:
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                x, y = r + dr, c + dc
                while 0 <= x < m and 0 <= y < n and grid[x][y] not in [1, 2]:
                    if grid[x][y] == 0:
                        grid[x][y] = 3
                    x, y = x + dr, y + dc
        return sum(row.count(0) for row in grid)