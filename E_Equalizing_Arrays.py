def equal():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    A = list(map(int, data[1:n+1]))
    m = int(data[n+1])
    B = list(map(int, data[n+2:n+2+m]))

    if sum(A) != sum(B):  
        print(-1)
        return

    i,j = 0,0
    sum_A, sum_B = 0, 0  
    segments = 0

    while i < n or j < m:
        if sum_A == sum_B and sum_A != 0:  
            segments += 1
        if sum_A < sum_B or (i < n and j >= m):
            sum_A += A[i]
            i += 1
        else:
            sum_B += B[j]
            j += 1

    print(segments + 1) 

equal()