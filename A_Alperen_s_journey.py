t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    x = 0
    y = 0
    found = False
    for ch in s:
        if ch == "U":
            y += 1
        elif ch == "D":
            y -= 1
        elif ch == "L":
            x -= 1
        elif ch == "R":
            x += 1
        if x == 1 and y == 1:
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")
