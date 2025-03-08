n,s = map(int, input().split())

if s % n !=0:
    print(s // n + 1)
else:
    print(s // n)