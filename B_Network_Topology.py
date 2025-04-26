def topology():
    import sys

    sys.setrecursionlimit(10**6)
    n, m = map(int, input().split())

    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)
        degree[x] += 1
        degree[y] += 1

    visited = [False] * (n + 1)

    def dfs(v):
        visited[v] = True
        for u in adj[v]:
            if not visited[u]:
                dfs(u)

    dfs(1)

    if not all(visited[1:]):
        print("unknown topology")
        return

    deg_count = {}
    for d in degree[1:]:
        deg_count[d] = deg_count.get(d, 0) + 1

    if m == n - 1 and deg_count.get(1, 0) == 2 and deg_count.get(2, 0) == n - 2:
        print("bus topology")
    elif m == n and deg_count.get(2, 0) == n:
        print("ring topology")
    elif m == n - 1 and deg_count.get(1, 0) == n - 1 and deg_count.get(n - 1, 0) == 1:
        print("star topology")
    else:
        print("unknown topology")


topology()
