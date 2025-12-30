from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def magic(r, c):
            if grid[r][c] != 5:
                return 0
            nums = [grid[r+i][c+j] for i in [-1,0,1] for j in [-1,0,1]]
            if sorted(nums) != list(range(1, 10)):
                return 0
            for i in [-1,0,1]:
                if sum(grid[r+i][c-1:c+2]) != 15:
                    return 0
            for j in [-1,0,1]:
                if sum(grid[r+i][c+j] for i in [-1,0,1]) != 15:
                    return 0
            if grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1] != 15:
                return 0
            if grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1] != 15:
                return 0

            return 1
        for r in range(1, m-1):
            for c in range(1, n-1):
                res += magic(r, c)
        return res
