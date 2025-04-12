from collections import deque


def lakes(test):
    ans = []
    for case in test:
        n, m, grid = case
        visit = [[False] * m for _ in range(n)]

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visit[x][y] = True
            volume = grid[x][y]

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                i, j = q.popleft()
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if not visit[ni][nj] and grid[ni][nj] > 0:
                            visit[ni][nj] = True
                            volume += grid[ni][nj]
                            q.append((ni, nj))
            return volume

        maxx = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and not visit[i][j]:
                    maxx = max(maxx, bfs(i, j))

        ans.append(maxx)

    return ans


t = int(input())
test = []

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test.append((n, m, grid))

ans = lakes(test)
for res in ans:
    print(res)
