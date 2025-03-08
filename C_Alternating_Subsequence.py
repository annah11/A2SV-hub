def max_alternating_sum():
    n = int(input())
    for _ in range(n):
        k = int(input())
        a = list(map(int, input().split()))
        cur_max = a[0]
        result = 0
        for i in range(1,k):
            if a[i] * a[i-1] > 0:
                cur_max = max(cur_max, a[i])
            else:
                result += cur_max
                cur_max = a[i]
        result += cur_max
        print(result)
                
max_alternating_sum()