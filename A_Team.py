def team():
    n = int(input())
    mat = [list(map(int,input().split())) for _ in range(n)]
    res = 0
    for i in range(n):
        if sum(mat[i])>=2:
            res += 1
    print(res)
team() 
