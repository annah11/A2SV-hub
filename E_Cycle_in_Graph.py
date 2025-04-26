import sys
import threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


def main():
    n, m, k = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    vis = set()
    stack = []
    found = [False]

    def dfs(node, parent):
        if found[0]:
            return
        vis.add(node)
        stack.append(node)
        for nb in graph[node]:
            if nb == parent:
                continue
            if nb not in vis:
                dfs(nb, node)
                if found[0]:
                    return
            else:
                if nb in stack:
                    idx = stack.index(nb)
                    cycle = stack[idx:]
                    if len(cycle) >= k + 1:
                        print(len(cycle))
                        print(*cycle)
                        found[0] = True
                        return
        stack.pop()

    for i in range(1, n + 1):
        if i not in vis:
            dfs(i, -1)
            if found[0]:
                break


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 25)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
