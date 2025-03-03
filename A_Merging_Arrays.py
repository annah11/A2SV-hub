def merging():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res =[]
    left = 0
    right =0
    while left < n and  right < m:

            
        if a[left] <= b[right]:
            res.append(a[left])
            left+=1
        else:
            res.append(b[right])
            right +=1
    if left == n:
        res.extend(b[right:])   
    else:
        res.extend(a[left:])
    # res = a+b
    # res.sort()
    
    return res
print(*merging())
# print(*res)
# merging(a,b)