def is_valid_minesweeper(n, m, grid):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    def count_bombs(x, y):
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '*':
                count += 1
        return count

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                continue
            elif grid[i][j] == '.':
                if count_bombs(i, j) > 0:
                    print("NO")
                    return
            else:
                if count_bombs(i, j) != int(grid[i][j]):
                    print("NO")
                    return
    
    print("YES")

n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

is_valid_minesweeper(n, m, grid)