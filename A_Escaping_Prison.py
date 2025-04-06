t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    total = 0
    for _ in range(n):
        w, l = map(int, input().split())
        total += max(w, l)
    if total >= h:
        print("YES")
    else:
        print("NO")
