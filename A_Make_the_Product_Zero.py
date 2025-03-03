def zero():
    n = int(input())
    x = list(map(int, input().split()))
    if 0 in x:
        print(0)
        return
    min_X =min(abs(y) for y in x)
    print(min_X) 
zero()