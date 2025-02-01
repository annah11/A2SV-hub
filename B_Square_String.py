n = int(input())
for i in range(n):
    s = str(input())
    if len(s) % 2 ==0 :
        half  = len(s) // 2
        if s[:half] == s[half:]:
            print("YES")
        else:
            print("NO") 
    else:
        print("NO")