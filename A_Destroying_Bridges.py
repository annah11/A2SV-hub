def bridge():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        shinigami = n
        for c in range(1, n + 1):
            if c * (n - c) <= k:
                shinigami = c
                break
        print(shinigami)


bridge()
