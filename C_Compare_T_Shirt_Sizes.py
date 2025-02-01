n = int(input().strip())  

for _ in range(n):
    a, b = input().split() 

    if a == b:
        print("=")
        continue

    if a[-1] == 'M':
        print(">" if b[-1] == 'S' else "<")
        continue
    if b[-1] == 'M':
        print("<" if a[-1] == 'S' else ">")
        continue

    count_a = a.count('X')
    count_b = b.count('X')

    if a[-1] == 'L' and b[-1] != 'L':
        print(">")
    elif b[-1] == 'L' and a[-1] != 'L':
        print("<")
    elif a[-1] == 'S' and b[-1] != 'S':
        print(">")
    elif b[-1] == 'S' and a[-1] != 'S':
        print(">")
    else:
        if count_a > count_b:
            print(">" if a[-1] == 'L' else "<")
        elif count_b > count_a:
            print("<" if a[-1] == 'L' else ">")
        else:
            print("=")
