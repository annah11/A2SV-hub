t = int(input())
for _ in range(t):
    xs = []
    ys = []
    for i in range(4):
        x,y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    s = max(xs) - min(xs)
    print(s*s)