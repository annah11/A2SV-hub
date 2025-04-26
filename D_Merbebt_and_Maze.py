import sys
from collections import deque


def merbebt():
    input = sys.stdin.read().split()
    ptr = 0
    t = int(input[ptr])
    ptr += 1
    for _ in range(t):
        while ptr < len(input) and input[ptr] == "":
            ptr += 1
        if ptr >= len(input):
            break

        n, k = map(int, input[ptr : ptr + 2])
        ptr += 2
        friends = list(map(int, input[ptr : ptr + k]))
        ptr += k
        adj = [[] for _ in range(n + 1)]
        for __ in range(n - 1):
            u, v = map(int, input[ptr : ptr + 2])
            ptr += 2
            adj[u].append(v)
            adj[v].append(u)

        leaves = []
        for i in range(1, n + 1):
            if len(adj[i]) == 1 and i != 1:
                leaves.append(i)

        root_dist = [-1] * (n + 1)
        q = deque()
        q.append(1)
        root_dist[1] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if root_dist[v] == -1:
                    root_dist[v] = root_dist[u] + 1
                    q.append(v)

        friend_dist = [-1] * (n + 1)
        q = deque()
        for x in friends:
            friend_dist[x] = 0
            q.append(x)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if friend_dist[v] == -1:
                    friend_dist[v] = friend_dist[u] + 1
                    q.append(v)

        possible = False
        for leaf in leaves:
            if root_dist[leaf] < friend_dist[leaf]:
                possible = True
                break
        print("YES" if possible else "NO")


merbebt()
