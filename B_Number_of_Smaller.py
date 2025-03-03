n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res =[]
first = 0
for sec in range(m):
    while first < n and a[first] < b[sec]:
        first +=1
    res.append(first)
        
# print(res)
print(*res)


        