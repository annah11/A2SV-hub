n, x = map(int, input().split())
dis = 0
for _ in range(n):
    sign, d = input().split()
    d = int(d)

    if sign == '+':  
        x += d 
    else: 
        if x >= d:  
            x -= d  
        else:
            dis += 1  

print(x, dis)