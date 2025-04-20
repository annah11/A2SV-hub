class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]):
                return False

            temp = board[r][c]
            board[r][c] = '#'

            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                if dfs(r + dr, c + dc, idx + 1):
                    return True

            board[r][c] = temp 
            return False

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False
