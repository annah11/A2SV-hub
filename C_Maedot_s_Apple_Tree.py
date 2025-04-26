import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    MAX = 2 * 10**5 + 5
    adj = [[] for _ in range(MAX)]
    leaf_count = [0] * MAX

    def dfs(u, parent):
        is_leaf = True
        leaf_count[u] = 0
        for v in adj[u]:
            if v != parent:
                is_leaf = False
                dfs(v, u)
                leaf_count[u] += leaf_count[v]
        if is_leaf:
            leaf_count[u] = 1

    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(1, n + 1):
            adj[i].clear()
            leaf_count[i] = 0
        for _ in range(n - 1):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        dfs(1, -1)
        q = int(input())
        for _ in range(q):
            x, y = map(int, input().split())
            print(leaf_count[x] * leaf_count[y])


if __name__ == "__main__":
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
