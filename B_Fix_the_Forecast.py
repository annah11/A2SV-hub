def forecast():
    t = int(input().strip())
    
    for _ in range(t):
        n, k = map(int,input().split())

        a = list(map(int, input().split()))

        b = list(map(int, input().split()))

        indexed_a = sorted((val, idx) for idx, val in enumerate(a))
        # for id,v in enumerate(a):
        #     indexed_a = sorted((v,id))
        
        b.sort()

        result = [0] * n
        for i in range(n):
            result[indexed_a[i][1]] = b[i]
            if indexed_a[i][0] == a[i-1]:
                result[indexed_a[i][1]] = result[indexed_a[i-1][1]]
        print(*result)
forecast()


