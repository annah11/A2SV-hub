def mad(x):
    d = int(str(x)[0])  
    digit = len(str(x)) 
    return sum(range(1, digit + 1)) + (d - 1) * 10

t = int(input())
for _ in range(t):
    x = int(input())
    print(mad(x))
