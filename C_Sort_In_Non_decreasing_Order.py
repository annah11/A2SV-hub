t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    for i in range(n):
      while i > 0 and a[i] =p[i]:
        a[i], a[i-1] = a[i-1], a[i]
        i -= 1
    if a == sorted(a):
        print("YES")
    else:
      print("NO")
      # print(a)
    # print(a)