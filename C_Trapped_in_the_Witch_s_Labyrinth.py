import sys

sys.setrecursionlimit(1 << 25)


def solve():
    t = int(sys.stdin.readline())

    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        grid = []
        for _ in range(n):
            line = sys.stdin.readline().strip()
            grid.append(list(line))

        parent = []
        rank = []
        size = []

        for i in range(n * m):
            parent.append(i)
            rank.append(0)
            size.append(1)

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            u_root = find(u)
            v_root = find(v)
            if u_root == v_root:
                return
            if rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
                size[u_root] += size[v_root]
            else:
                parent[u_root] = v_root
                size[v_root] += size[u_root]
                if rank[u_root] == rank[v_root]:
                    rank[v_root] += 1

        # Process the grid and create unions based on the directions
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                if c == "?":
                    continue
                di, dj = dirs[c]
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    u = i * m + j
                    v = ni * m + nj
                    union(u, v)

        exit_cells = set()
        for i in range(n):
            for j in range(m):
                c = grid[i][j]
                if c == "?":
                    continue
                di, dj = dirs[c]
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < m):
                    exit_cells.add(find(i * m + j))

        visited = [False] * (n * m)
        res = 0

        for i in range(n):
            for j in range(m):
                u = i * m + j
                root = find(u)
                if root in exit_cells:
                    continue
                if not visited[root]:
                    visited[root] = True
                    res += size[root]

        print(res)


solve()
