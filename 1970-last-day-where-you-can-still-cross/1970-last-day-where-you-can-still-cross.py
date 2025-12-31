class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can(day):
            grid = [[0]*col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1

            q = deque()
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    grid[0][j] = 1

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]
            while q:
                x, y = q.popleft()
                if x == row - 1:
                    return True
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
            return False

        l, r = 0, len(cells)
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if can(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
