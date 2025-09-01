class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        next_val = {1: 2, 2: 0, 0: 2}
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        @lru_cache(None)
        def dfs(i, j, turned, val, d):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == val):
                return 0
            nv = next_val[val]
            di, dj = directions[d]
            max_len = 1 + dfs(i + di, j + dj, turned, nv, d)

            if not turned:
                new_di, new_dj = dj, -di
                try:
                    nd = directions.index((new_di, new_dj))
                except ValueError:
                    nd = None
                if nd is not None:
                    max_len = max(max_len, 1 + dfs(i + new_di, j + new_dj, True, nv, nd))
            return max_len

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        res = max(res, dfs(i, j, False, 1, d))
        return res