def max_alternating_sum():
    n = int(input())
    for _ in range(n):
        k = int(input())
        a = list(map(int, input().split()))
        postive = 0
        negative = 0
        ans = []
        cur_max = 0
        maxx = 0
        for i in range(k):
            if a[i] > 0:
                postive += a[i]
            else:
                negative += a[i]
                
        
        
max_alternating_sum()