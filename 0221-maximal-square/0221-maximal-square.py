class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rl = len(matrix)
        cl = len(matrix[0])
        grid =[ [0]*(cl+1 )for _ in range(rl+1)]
        ans = 0
        for i in range(rl):
            for j in range(cl):
                if matrix[i][j] == "1":
                    grid[i+1][j+1] = min(grid[i][j], grid[i+1][j], grid[i][j+1]) + 1
                    ans = max(grid[i+1][j+1]**2,ans)

        return ans