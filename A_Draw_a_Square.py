def is_square(l, r, d, u):
    if l == r == d == u:
        return "Yes" 
    else:
        return "No"

t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    print(is_square(l, r, d, u))
