n = int(input())
stones = list(map(int, input().split()))
_orignal = [0] * (n+1)
for i in range(n+1):
    _orignal[i] +=_orignal[i-1] + stones[i-1]
sorted_stones = sorted(stones)
_sorted = [0] * (n+1)
for i in range(n+1):
    _sorted[i] +=_sorted[i-1] + sorted_stones[i-1]
m = int(input())
result = []
for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        result.append(_orignal[r] - _orignal[l-1])
    else:
        result.append(_sorted[r] - _sorted[l-1])
print(*result, sep='\n')