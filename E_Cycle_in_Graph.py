from collections import defaultdict


def find_cycle(n, m, k, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (n + 1)
    parent = [-1] * (n + 1)
    depth = [0] * (n + 1)

    stack = []

    for start in range(1, n + 1):
        if not visited[start]:
            stack.append((start, -1))
            while stack:
                u, par = stack.pop()
                if visited[u]:
                    continue
                visited[u] = True
                parent[u] = par
                if par != -1:
                    depth[u] = depth[par] + 1

                for v in graph[u]:
                    if not visited[v]:
                        stack.append((v, u))
                    elif v != par and depth[u] - depth[v] + 1 >= k + 1:
                        cycle = [u]
                        cur = u
                        while cur != v:
                            cur = parent[cur]
                            cycle.append(cur)
                        print(len(cycle))
                        print(" ".join(map(str, cycle)))


n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
find_cycle(n, m, k, edges)
