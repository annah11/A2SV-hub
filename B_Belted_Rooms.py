def snake():
    import sys

    sys.setrecursionlimit(10**6)
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()
        if ">" not in s or "<" not in s:
            print(n)
            continue
        graph = [[] for _ in range(n)]
        for i in range(n):
            if s[i] == "-":
                u = i
                v = (i + 1) % n
                graph[u].append(v)
                graph[v].append(u)

        visited = [False] * n
        returnable = [False] * n

        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        for i in range(n):
            if not visited[i]:
                component = []
                dfs(i, component)
                if len(component) > 1:
                    for room in component:
                        returnable[room] = True
        for i in range(n):
            if s[i] == "-" or s[(i - 1 + n) % n] == "-":
                returnable[i] = True

        print(sum(returnable))


snake()
