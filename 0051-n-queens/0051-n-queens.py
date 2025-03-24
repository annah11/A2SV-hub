class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(i: int, g, col, dg, udg):
            if i == n:
                ans.append(["".join(row) for row in g])
                return
            for j in range(n):
                if col[j] == 0 and dg[i + j] == 0 and udg[i - j + n - 1] == 0:
                    g[i][j] = "Q"
                    col[j] = dg[i + j] = udg[i - j + n - 1] = 1
                    dfs(i + 1, g, col, dg, udg)
                    g[i][j] = "."
                    col[j] = dg[i + j] = udg[i - j + n - 1] = 0
        
        ans = []
        g = [["."] * n for _ in range(n)]
        col = [0] * n
        dg = [0] * (2 * n - 1)
        udg = [0] * (2 * n - 1)

        dfs(0, g, col, dg, udg)
        return ans
