n,m,k = [int(i) for i in input().split()]
l = 1
r =n*m
ans = None
while l<=r:
    mid = (l +r)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(m,mid//i)
    if cnt >=k:
        ans = mid
        r = mid -1
    else:
        l= mid+1
print(ans)