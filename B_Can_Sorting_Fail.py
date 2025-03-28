def  can(n,arr):
    arr_sor = sorted(arr)
    for i in range(n - 1):
        if arr[i] != arr_sor[i]:
            return "YES"
    return "NO"
t= int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    print(can(n,arr))

