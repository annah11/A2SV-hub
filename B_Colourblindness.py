t = int(input())
for _ in range(t):
    col = int(input())
    s = input()
    s1 = input()
    valid = True
    for i in range(col):
        if s[i] == s1[i]:
            continue
        elif (s[i] == "B" and s1[i] == "G") or (s[i] == "G" and s1[i] == "B"):
            continue
 
        else:
            valid = False
            break
    if valid:
        print("YES")
    else:
        print("NO")