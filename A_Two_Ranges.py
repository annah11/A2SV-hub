q = int(input())
for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    if l1 == l2:
        l1 += 1
        r1 += 1
    print(l1, l2)
