def cyclic():
    import sys

    sys.setrecursionlimit(2 * 10**5 + 10)
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    from collections import defaultdict

    graph = defaultdict(list)

    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        index += 2
        graph[u].append(v)
        graph[v].append(u)

    vis = [False] * n

    def dfs(node, component):
        vis[node] = True
        component.append(node)
        for ni in graph[node]:
            if not vis[ni]:
                dfs(ni, component)

    result = 0
    for node in range(n):
        if not vis[node]:
            component = []
            dfs(node, component)

            is_cycle = True
            if len(component) < 3:
                continue
            for v in component:
                if len(graph[v]) != 2:
                    is_cycle = False
                    break
            if is_cycle:
                result += 1

    print(result)


cyclic()
