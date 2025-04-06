t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(a[i] - a[j])
            res = max(res, diff)
    print(res)
