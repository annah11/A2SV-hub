t = int(input())
for _ in range(t):
    n, f, a, b = map(int, input().split())
    messages = list(map(int, input().split()))
    
    prev = 0
    remaining = f
    possible = True
    
    for m in messages:
        gap = m - prev
        cost = a * gap
        if cost > b:
            cost = b
        remaining -= cost
        if remaining <= 0:
            possible = False
            break
        prev = m
        
    print("YES" if possible else "NO")
