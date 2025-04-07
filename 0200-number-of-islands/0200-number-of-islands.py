class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def inbound(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)

        return cnt
