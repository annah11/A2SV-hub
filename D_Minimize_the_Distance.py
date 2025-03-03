def minimize_distance():
    n = int(input())
    x = list(map(int, input().split()))
    
    x.sort() 
    print(x[(n - 1) // 2]) 
minimize_distance()
