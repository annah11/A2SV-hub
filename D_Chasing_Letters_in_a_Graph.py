from collections import Counter

n, m = map(int, input().split())
a = input().strip()
cnt = Counter(a)

if max(cnt.values()) == 1:
    print(-1)
else:
    print(max(cnt.values()))
