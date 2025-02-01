n = int(input().strip())
t = input().strip()    
s = ""
index = 0
step = 1
    
while index < n:
    s += t[index]
    index += step
    step += 1
    
print(s)
