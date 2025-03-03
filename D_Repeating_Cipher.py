n = int(input())
t = str(input())
s = ""
step = 1
index = 0 
while index < n:
    s +=t[index]
    index += step
    step += 1
print(s)