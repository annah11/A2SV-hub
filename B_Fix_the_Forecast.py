def forecast():
    t = int(input().strip())
    
    for _ in range(t):
        n, k = map(int,input().split())

        a = list(map(int, input().split()))

        b = list(map(int, input().split()))

        indexed_a = sorted((val, idx) for idx, val in enumerate(a))
 
        
        b.sort()

        result = [0] * n
        for i in range(n):
            val, idx = indexed_a[i]
            result[idx] = b[i]  
        print(*result)
forecast()
    