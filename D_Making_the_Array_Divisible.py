from collections  import defaultdict
t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = defaultdict(int)
    
    for a in arr:
        rem = a % k
        if rem != 0:
            d = k - rem
            cnt[d] += 1

    _max = 0
    for d, count in cnt.items():
        car = d + (count - 1) * k
        _max = max(_max, car)
    
    print(_max+1 if _max else 0)
