n = int(input())
for x in range(n):
    s = str(input())
    check = "codeforces"
    
    count = 0
    for i in range (10):
        if s[i] != check[i]:
            count += 1

 
    print(count)
            