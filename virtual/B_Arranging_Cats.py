t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().strip()))
    must = list(map(int, input().strip()))
    less = 0
    greater = 0
    for i in range(n):
        if arr[i] != must[i]:
            if arr[i] < must[i]:
                less +=1
            else:
                greater +=1
    print(max(less,greater))

