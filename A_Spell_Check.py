t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    check = "Timur"
    for i in range(n):
        if len(s) !=5:
            print("NO") 
            break
        if sorted(s) == sorted(check):
            print("YES")
            break
        else:
            print("NO")
            break