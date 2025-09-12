t = int(input())
for _ in range(t):
    s = input().strip()
    x_len= 0
    d = 0
    for ch in s:
        if ch == 'L':
            d += 1
            x_len = max(x_len, d)
        else:
            d = 0
    print(x_len + 1)
