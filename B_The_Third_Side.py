t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    result = sum(arr) - (n - 1)
    print(result)
