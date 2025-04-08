class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # return 
        if not board or not board[0]: return

        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                board[r][c] != 'O' or (r, c) in visited):
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        def scan_border(row=0, col=0):
            if row >= rows: return
            if col >= cols:
                scan_border(row + 1, 0)
                return
            if (row == 0 or row == rows - 1 or col == 0 or col == cols - 1):
                dfs(row, col)
            scan_border(row, col + 1)

        scan_border()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'
